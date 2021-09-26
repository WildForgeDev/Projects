var apiKey = 'zn6b2NpM02U0quaYfFu6Uo24wNGwBIs0';
var centerCoords = [-104.799973, 38.901104];
var map = tt.map({
    key: apiKey,
    container: 'map',
    center: centerCoords,
    style: '/static/pizzapp/js/mono.json',
    zoom: 11
});

var MILLIS_IN_SECOND = 1000;
var DELIVERY_TIME_IN_MINUTES = 45;
var MIN_SLIDER_RANGE = 480;
var MAX_SLIDER_RANGE = 1320;
var reachableRangeBudgetTimeInSeconds = 60 * DELIVERY_TIME_IN_MINUTES;
var pizzaPrefixId = 'pizza-';
var polygonLayers = [];
var pizzaMarkers = [];
var clientMarker;
var deliveryTimeSlider;
var trafficFlowTilesTier;


function initControlMenu() {
      var commonOptions = {
          key: apiKey,
          center: map.getCenter(),
          radius: 1000
      };
      var searchBoxInstance = new tt.plugins.SearchBox(tt.services, {
          minNumberOfCharacters: 0,
          searchOptions: commonOptions,
          autocompleteOptions: commonOptions
      });
      document.getElementById('search-panel').append(searchBoxInstance.getSearchBoxHTML());
      deliveryTimeSlider = new Slider('#slider-input', {
          min: MIN_SLIDER_RANGE,
          max: MAX_SLIDER_RANGE,
          value: MIN_SLIDER_RANGE,
          step: 15,
          tooltip: 'hide',
          enabled: false,
          rangeHighlights: [
              { start: 510, end: 810, class: 'medium-traffic' },
              { start: 540, end: 705, class: 'high-traffic' }
          ]
      });
      deliveryTimeSlider.on('change', function (event) {
          document.getElementById('delivery-time').innerText = convertSliderValueToTimeString(event.newValue);
      }, false);
      deliveryTimeSlider.on('slideStop', function () {
          setDeliveryTimeSliderValue();
          setDeliveryTimeSpanValue();
      });
      document.getElementById('calculate-range').addEventListener('click', displayReachableRangePolygons);
      document.getElementById('delivery-toggle').addEventListener('change', toggleDelayedDelivery);
      document.getElementById('traffic-toggle').addEventListener('change', toggleTrafficFlowLayer);
      searchBoxInstance.on('tomtom.searchbox.resultselected', showClientMarkerOnTheMap);
  }

initControlMenu();

function convertSliderValueToTimeString(sliderValue) {
      var hours = Math.floor(sliderValue / 60);
      var minutes = sliderValue % 60;
      if (hours < 10) {
          hours = '0' + hours;
      }
      if (minutes < 10) {
          minutes = '0' + minutes;
      }
      return hours + ':' + minutes;
  }

  function setDeliveryTimeSliderValue() {
      var currentDate = new Date();
      var currentTimeInMinutesWithDeliveryTime = (currentDate.getHours() * 60) + currentDate.getMinutes() + DELIVERY_TIME_IN_MINUTES;
      if (deliveryTimeSlider.getValue() < currentTimeInMinutesWithDeliveryTime) {
          if (currentTimeInMinutesWithDeliveryTime < MIN_SLIDER_RANGE) {
              deliveryTimeSlider.setValue(MIN_SLIDER_RANGE);
          }
          else if (currentTimeInMinutesWithDeliveryTime > MAX_SLIDER_RANGE) {
              deliveryTimeSlider.setValue(MAX_SLIDER_RANGE);
          } else {
              var roundedCurrentTime = currentTimeInMinutesWithDeliveryTime % 15 === 0 ? currentTimeInMinutesWithDeliveryTime : Math.ceil(currentTimeInMinutesWithDeliveryTime / 15) * 15;
              deliveryTimeSlider.setValue(roundedCurrentTime);
          }
      }
  }

  function setDeliveryTimeSpanValue() {
      var deliveryTimeSpan = document.getElementById('delivery-time');
      if (deliveryTimeSlider.isEnabled()) {
          deliveryTimeSpan.innerText = convertSliderValueToTimeString(deliveryTimeSlider.getValue());
      } else {
          deliveryTimeSpan.innerText = '--:--';
      }
  }
  
function displayPizzaMarkers() {
      geojson.features.forEach(function (marker) {
          createMarker(marker);
      });
  }

  function createMarker(geoJsonPoint) {
      var position = geoJsonPoint.geometry.coordinates;
      const markerElement = document.createElement('div');
      markerElement.innerHTML = "";
      marker = new tt.Marker({
          draggable: true,
          element: markerElement
      }).setLngLat(position).addTo(map);
      marker.on('dragend', function () {
          if (polygonLayers.length > 0) {
              displayReachableRangePolygons();
          }
      });
      marker.polygonColor = geoJsonPoint.properties.polygonColor;
      pizzaMarkers.push(marker);
      return marker;
  }

  function displayReachableRangePolygons() {
  }
  
initControlMenu();
displayPizzaMarkers();

searchBoxInstance.on('tomtom.searchbox.resultselected', showClientMarkerOnTheMap);

function showClientMarkerOnTheMap(result) {
      document.getElementById('calculate-range').disabled = false;
      if (clientMarker) {
          map.removeLayer(clientMarker);
      }
      const markerElement = document.createElement('div');
      markerElement.innerHTML = "";
      var position = result.data.result.position;
      clientMarker = new tt.Marker({ element: markerElement }).setLngLat([position.lng, position.lat]).addTo(map);
      if (polygonLayers.length > 0) {
          displayReachableRangePolygons();
      }
  }
  
function displayReachableRangePolygons() {
     closeAllPopups();
     clearPolygonLayers();
     tt.services.calculateReachableRange({
         batchMode: 'sync',
         key: apiKey,
         batchItems: constructRangeBatchRequest()
     })
         .go()
         .then(function (polygons) {
             displayMarkerPolygons(polygons);
         });

     calculateTravelTime();
 }

 function constructRangeBatchRequest() {
     var queries = [];
     pizzaMarkers.forEach(function (marker) {
         var query = {
             origin: [marker.getLngLat().lng, marker.getLngLat().lat],
             timeBudgetInSec: reachableRangeBudgetTimeInSeconds
         };
         if (isDeliveryDelayed()) {
             var departureDeliveryDate = getDepartureDeliveryDate();
             if (departureDeliveryDate > new Date()) {
                 query.departAt = departureDeliveryDate;
             }
         }
         queries.push(query);
     });
     return queries;
 }

 function closeAllPopups() {
     pizzaMarkers.forEach(function(marker) {
         if (marker.getPopup().isOpen()) {
             marker.togglePopup();
         }
     })
 }

 function clearPolygonLayers() {
     polygonLayers.forEach(function (layer) {
         map.removeLayer(layer.id);
         map.removeSource(layer.id);
     })
     polygonLayers = [];
 }
 
function displayMarkerPolygons(polygons) {
        polygons.forEach(function (rangeData, index) {
            if (pizzaMarkers[index]) {
                addPolygonToMap("polygon_" + index, rangeData, pizzaMarkers[index].polygonColor)
            }
        });
    }

    function addPolygonToMap(id, rangeData, polygonColor) {
        let polygonLayer = buildStyle(id, rangeData.toGeoJson(), polygonColor);
        map.addLayer(polygonLayer);
        polygonLayer.id = id;
        polygonLayers.push(polygonLayer);
    }

    function buildStyle(id, data, color) {
        return {
            'id': id,
            'type': 'fill',
            'source': {
                'type': 'geojson',
                'data': data
            },
            'paint': {
                'fill-color': color,
                'fill-opacity': 0.68,
            },
            'layout': {}
        }
    }
	
document.getElementById('calculate-range').addEventListener('click', displayReachableRangePolygons);

function calculateTravelTime() {
      if (clientMarker && pizzaMarkers.length > 0) {
          tt.services.calculateRoute({
              batchMode: 'sync',
              key: apiKey,
              batchItems: constructBatchRequest()
          })
              .go()
              .then(displayBatchRoutingResults)
      }
  }
  
calculateTravelTime();
  
  
function constructBatchRequest() {
      var queries = [];
      pizzaMarkers.forEach(function (marker) {
          var query = {
              locations: [marker.getLngLat(), clientMarker.getLngLat()],
              computeTravelTimeFor: 'all'
          };
          if (isDeliveryDelayed()) {
              var departureDeliveryDate = getDepartureDeliveryDate();
              if (departureDeliveryDate > new Date()) {
                  query.departAt = departureDeliveryDate;
              }
          }
          queries.push(query);
      });
      return queries;
  }
  
function displayBatchRoutingResults(resultData) {
     var indexShortestTime;
     var shortestTime;
     resultData.forEach(function (routeData, index) {
         const routeGeoJson = routeData.toGeoJson();
         var pizzaElement = document.getElementById(pizzaPrefixId + (index + 1));
         pizzaElement.classList.remove('active');
         var travelTimesElements = pizzaElement.getElementsByClassName('travel-time-minutes');
         if (travelTimesElements.length > 0) {
             pizzaElement.removeChild(travelTimesElements[0]);
         }

         if (routeData && !routeData.error) {
             var travelTime = routeGeoJson.features[0].properties.summary.travelTimeInSeconds;
             if (!shortestTime || shortestTime > travelTime) {
                 indexShortestTime = index;
                 shortestTime = travelTime;
             }
             var travelTimeSpan = document.createElement('span');
             travelTimeSpan.innerHTML = Math.ceil(travelTime / 60).toString() + ' mins';
             travelTimeSpan.classList.add('travel-time-minutes');
             pizzaElement.appendChild(travelTimeSpan);
         }
     });
     if (typeof indexShortestTime !== 'undefined' || indexShortestTime !== null) {
         document.getElementById(pizzaPrefixId + (indexShortestTime + 1)).classList.add('active');
     }
     closeAllPopups();
     createAndBindPopups();
     pizzaMarkers[indexShortestTime].togglePopup();
 }
 
 
pizzaPrefixId + (index + 1);
 
function getDeliveryDateTime() {
      var timeParts = document.getElementById('delivery-time').innerText.split(':');
      var chosenDeliveryDate = new Date();
      chosenDeliveryDate.setHours(parseInt(timeParts[0]));
      chosenDeliveryDate.setMinutes(parseInt(timeParts[1]));
      return chosenDeliveryDate;
  }

  function getDepartureDeliveryDate() {
      return new Date(getDeliveryDateTime().getTime() - reachableRangeBudgetTimeInSeconds * MILLIS_IN_SECOND);
  }

  function isDeliveryDelayed() {
      return deliveryTimeSlider.isEnabled();
  }
  
  
if (isDeliveryDelayed()) {
      var departureDeliveryDate = getDepartureDeliveryDate();
      if (departureDeliveryDate > new Date()) {
          query.departAt = departureDeliveryDate;
      }
  }
  
  
document.getElementById('delivery-toggle').addEventListener('change', toggleDelayedDelivery);
  
function toggleDelayedDelivery() {
      deliveryTimeSlider.toggle();
      setDeliveryTimeSliderValue();
      setDeliveryTimeSpanValue();
  }
  
function createAndBindPopups() {
    pizzaMarkers.forEach(function (marker, index) {
        var pizzaMenuDiv = document.getElementById(pizzaPrefixId + (index + 1));
        var pizzaSpans = pizzaMenuDiv.getElementsByTagName('span');
        var pizzaString = '<span><b>' + pizzaSpans[0].textContent + '</b>';
        if (pizzaSpans.length > 1) {
            pizzaString += '<br>' + pizzaSpans[1].textContent;
        }
        pizzaString += '</span>';
        var customPopup = '<div class="pizza-balloon">' + pizzaString +
            '<img src="{% static 'pizzapp/images/icons/pizza_oven_illustration.png' %}" alt="pizza oven"/></div>';
        marker.setPopup(new tt.Popup({ offset: 35 }).setHTML(customPopup));
    });
}


initControlMenu();
displayPizzaMarkers();
createAndBindPopups();

function toggleTrafficFlowLayer() {
      if (document.getElementById('traffic-toggle').checked) {
          var flowConfig = {
              key: apiKey,
              style: 'tomtom://vector/1/relative',
              refresh: 30000
          };
          trafficFlowTilesTier = new tt.TrafficFlowTilesTier(flowConfig);
          map.addTier(trafficFlowTilesTier);
      }
      else {
          map.removeTier(trafficFlowTilesTier.getId());
      }
  }
  
  document.getElementById('traffic-toggle').addEventListener('change', toggleTrafficFlowLayer);