// This function is written iin Jquery and it finds all the menu sections and when you click on them it detects the
// click and switches the menu items you see on the page to the specific menu category you want to look at. Basically
// we add attributes to the html page in the html by grabbing those pieces of data from the view when it is rendered
// then we use those data attributes to hide or show menu items when we click. The data attributes on the HTML are what
// we call events and the function below is a handler for the event so an example is you click a button on the page,
// When Javascript or Jquery in this case detects the user action it performs the function of showing the menu category
// the customer wants to see and hides the data they don't want to see.
$(document).on('click', ".btn-check",function(){
    let id = $(this).attr("data-id");
    $(".card").hide();
    $("[data-type="+id+"]").show();
})

// This is our function to handle the add fromm cart and remove from cart, The Javascript here listens for a button
// click on all the buttons with the update cart attribute. It then gets the action of the button and the product id or
// cart id depending on the action you are performing and runs one of the functions further below to send the data back
// to the view and render changes to the page without a refresh all while updating the database records throught the
// back end views file.
 $(document).on('click','.update-cart',function(){
     let action = $(this).attr("data-action");
     let productid = $(this).attr("data-product");
     // console.log(productid)
     let cart_id = $(this).attr("data-cartitem");
     // console.log(cart_id, productid, action);
     if(user === 'AnonymousUser') {
         if (action === "add") {
             AddUserOrderGuest(productid, action)
         }
         if (action=== "remove"){
             removeUserOrderGuest(cart_id, action)
             $("[data-cart-row="+cart_id+"]").hide();
         }
     }else{
         if (action === "add") {
             AddUserOrderLoggedIn(productid, action)
         }
         if (action=== "remove"){
             RemoveUserOrderLoggedIn(cart_id, action)
             $("[data-cart-row="+cart_id+"]").hide();
         }
     }
     })


// As the function name implies this adds a cart item to the users order through asynchronous javascript sending a post
// call to the update orders function in views.py. We use the data attributes added to the html elements to pull the
// data attributes, we take that data and in our success response further down we set the variables from our data from
// the backend views.py file and update the records on the page with the data. The other four functions below do the
// same thing except there are variations on if the action is adding or removing an item or if the user is logged in
// or not. The idea behind this is the same but the methods by which we get to the end result differ slightly.
function AddUserOrderLoggedIn(productId, action){
    console.log('User is authenticated, sending data...')
    let url = '/update_item/'

    fetch (url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) =>{
            return response.json();
        })
        .then((data) =>{
            console.log(' here is Data: ', data);
            let subtotal = data.order_subtotal;
            let delivery_fee = data.order_delivery_fee;
            let tax = data.order_tax;
            let order_grand_total = data.order_grand_total;
            let product_name = data.product_name;
            let quantity = 1;
            let cart_id = data.cart_id;
            console.log(cart_id);
            document.getElementById('subtotal_number').firstChild.data = "$" + subtotal;
            document.getElementById('delivery_fee_number').firstChild.data = "$" + delivery_fee;
            document.getElementById('tax_number').firstChild.data = "$" + tax;
            document.getElementById('grand_total_number').firstChild.data = "$" + order_grand_total;
            let table = document.getElementById('product_table_id');
            let newRow = table.insertRow(-1);
            newRow.setAttribute('data-cart-row', cart_id);
            newRow.setAttribute('class', 'cart-item-row');
            let newCell1 = newRow.insertCell();
            let newCell2 = newRow.insertCell();
            let newCell3 = newRow.insertCell();
            let newText1 = document.createTextNode(quantity + ' x ');
            let newText2 = document.createTextNode(product_name);
            let img = document.createElement('img');
            let test = document.createElement('a')
            img.src = '/static/pizzapp/images/icons/red-x.png'
            img.alt = 'remove'
            newCell1.setAttribute('class', 'card-text quantity_item')
            newCell1.setAttribute('id', 'quantity_item_id')
            newCell2.setAttribute('class','card-text cart_item' )
            newCell2.setAttribute('id','cart_item_id' )
            newCell3.setAttribute('class', 'card-text remove_item update-cart');
            newCell3.setAttribute('data-cartitem', cart_id);
            newCell3.setAttribute('data-action', 'remove');
            test.setAttribute('href', '#')
            newCell1.appendChild(newText1);
            newCell2.appendChild(newText2);
            newCell3.appendChild(test)
            test.appendChild(img)
            // console.log("You are getting there.");
        });
}


// See above for deeper explanation - in this function we are adding a cart item to a user order for a non logged in
// user and updating the page dynamically.
function AddUserOrderGuest(productId, action){
    console.log('User is a guest, sending data...')
    let url = '/update_item/'

    fetch (url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) =>{
            return response.json();
        })
        .then((data) =>{
            // console.log(' here is Data: ', data);
            let subtotal = data.order_subtotal;
            let delivery_fee = data.order_delivery_fee;
            let tax = data.order_tax;
            let order_grand_total = data.order_grand_total;
            let product_name = data.product_name;
            let quantity = 1;
            let cart_id = data.cart_id;
            // console.log(cart_id);
            document.getElementById('subtotal_number').firstChild.data = "$" + subtotal;
            document.getElementById('delivery_fee_number').firstChild.data = "$" + delivery_fee;
            document.getElementById('tax_number').firstChild.data = "$" + tax;
            document.getElementById('grand_total_number').firstChild.data = "$" + order_grand_total;
            let table = document.getElementById('product_table_id');
            let newRow = table.insertRow(-1);
            newRow.setAttribute('data-cart-row', cart_id);
            newRow.setAttribute('class', 'cart-item-row');
            let newCell1 = newRow.insertCell();
            let newCell2 = newRow.insertCell();
            let newCell3 = newRow.insertCell();
            let newText1 = document.createTextNode(quantity + ' x ');
            let newText2 = document.createTextNode(product_name);
            let img = document.createElement('img');
            let test = document.createElement('a')
            img.src = '/static/pizzapp/images/icons/red-x.png'
            img.alt = 'remove'
            newCell1.setAttribute('class', 'card-text quantity_item')
            newCell1.setAttribute('id', 'quantity_item_id')
            newCell2.setAttribute('class','card-text cart_item' )
            newCell2.setAttribute('id','cart_item_id' )
            newCell3.setAttribute('class', 'card-text remove_item update-cart');
            newCell3.setAttribute('data-cartitem', cart_id);
            newCell3.setAttribute('data-action', 'remove');
            test.setAttribute('href', '#')
            newCell1.appendChild(newText1);
            newCell2.appendChild(newText2);
            newCell3.appendChild(test)
            test.appendChild(img)
            // console.log("You are getting there.");
        });
}

// See above for deeper explanation - in this function we are removing a cart item from a user order for a non logged in
// user and updating the page dynamically.
function removeUserOrderGuest(cart_id, action) {
    console.log('User is logged in, sending data...')
    console.log(cart_id, action)
    let url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'cart_id': cart_id, 'action': action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // console.log(' here is Data: ', data)
            let subtotal = data.order_subtotal;
            let delivery_fee = data.order_delivery_fee;
            let tax = data.order_tax;
            let new_grand_total = data.order_grand_total;
            let cart_id = data.cart_id;
            console.log(subtotal, delivery_fee, tax, new_grand_total)
            document.getElementById('subtotal_number').firstChild.data = "$" + subtotal;
            document.getElementById('delivery_fee_number').firstChild.data = "$" + delivery_fee;
            document.getElementById('tax_number').firstChild.data = "$" + tax;
            document.getElementById('grand_total_number').firstChild.data = "$" + new_grand_total;
        });
}


// See above for deeper explanation - in this function we are removing a cart item from a user order for a logged in
// user and updating the page dynamically.
function RemoveUserOrderLoggedIn(cart_id, action){
    // console.log('User is logged in, sending data...')
    let url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'cart_id': cart_id, 'action': action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // console.log(' here is Data: ', data)
            let subtotal = data.order_subtotal;
            let delivery_fee = data.order_delivery_fee;
            let tax = data.order_tax;
            let new_grand_total = data.order_grand_total;
            let cart_id = data.cart_id;
            console.log(subtotal, delivery_fee, tax, new_grand_total)
            document.getElementById('subtotal_number').firstChild.data = "$" + subtotal;
            document.getElementById('delivery_fee_number').firstChild.data = "$" + delivery_fee;
            document.getElementById('tax_number').firstChild.data = "$" + tax;
            document.getElementById('grand_total_number').firstChild.data = "$" + new_grand_total;
        });
}

$(document).ready(function() {
  if (!$("#mySelect option:selected").length) {
    $("#mySelect option[value='3']").attr('selected', 'selected');
  }
});

$(document).ready(function(){
        $(".credit-card-payment").hide();
        $(".charge-to-manager-payment").hide();
        $(".cash-on-delivery").hide();
    $('#payment-select').on('change', function() {
      if ( this.value === '2') {
        $(".credit-card-payment").show();
        $(".charge-to-manager-payment").hide();
        $(".cash-on-delivery").hide();
      } else if( this.value === '3') {
          $(".credit-card-payment").hide();
          $(".charge-to-manager-payment").show();
          $(".cash-on-delivery").hide();
      }else if( this.value === '1'){
          $(".credit-card-payment").hide();
          $(".charge-to-manager-payment").hide();
          $(".cash-on-delivery").show();
      }
    });
});

// $(document).on('click','.submit_cc_payment',function(){