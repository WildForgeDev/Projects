import java.awt.event.ActionEvent;

import java.awt.event.ActionListener;

public class PriceController {

            private PriceView theView;

            private PriceModel theModel;

            public PriceController(PriceView theView, PriceModel theModel) {

                        this.theView = theView;

                        this.theModel = theModel;

                        this.theView.addCalculateListener(new CalculateListener());

            }

            class CalculateListener implements ActionListener {

                        public void actionPerformed(ActionEvent e) {

                                    double itemPrice, taxRate = 0;

                                    try {

                                                itemPrice = theView.getItemPrice();

                                                taxRate = theView.getTaxRate();

                                                theModel.calcTotalPrice(itemPrice, taxRate);

                                                theView.setTotalPrice(theModel.getTotalPrice());

                                    }

                                    catch (NumberFormatException ex) {

                                                System.out.println(ex);

                                                theView.displayErrorMessage("Enter item price and tax rate.");

                                    }

                        }

            }

}
                                    