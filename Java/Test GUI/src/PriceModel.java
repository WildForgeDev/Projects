public class PriceModel {

            private double totalPrice;  

            public void calcTotalPrice(double itemPrice, double taxRate){

                        totalPrice = itemPrice * (1.0 + (taxRate * .01));

            }

            public double getTotalPrice(){

                        return totalPrice;                    

            }

}

