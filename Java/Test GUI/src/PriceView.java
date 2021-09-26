import java.awt.event.ActionListener;

import javax.swing.*;

public class PriceView extends JFrame {

            private JLabel priceLabel = new JLabel("Item Price:");

            private JTextField itemPrice = new JTextField(10);

            private JLabel multLabel = new JLabel("     *");

            private JLabel taxRateLabel = new JLabel("     Tax Rate(%):");

            private JTextField taxRate = new JTextField(10);

            private JButton calculateButton = new JButton("Calculate");

            private JLabel totalPriceLabel = new JLabel("     Total Price:");      

            private JTextField priceCalc = new JTextField(10);

            PriceView() {

                        JPanel calcPanel = new JPanel();

                        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

                        this.setSize(500, 150);           

                        this.setTitle("MVC - Calculate Total Price"); 

                        calcPanel.add(priceLabel);

                        calcPanel.add(itemPrice);

                        calcPanel.add(multLabel);

                        calcPanel.add(taxRateLabel);            

                        calcPanel.add(taxRate);

                        calcPanel.add(calculateButton);

                        calcPanel.add(totalPriceLabel);                                             

                        calcPanel.add(priceCalc);

                        this.add(calcPanel);

            }

            public double getItemPrice() {

                        return Double.parseDouble(itemPrice.getText());

            }

            public double getTaxRate() {

                        return Double.parseDouble(taxRate.getText());

            }

            public double getTotalPrice() {

                        return Double.parseDouble(priceCalc.getText());

            }

            public void setTotalPrice(double totalPrice) {

                        priceCalc.setText(Double.toString(totalPrice));

            }

            void addCalculateListener(ActionListener listenForCalcButton) {

                        calculateButton.addActionListener(listenForCalcButton);

            }

            void displayErrorMessage(String errorMessage) {

                        JOptionPane.showMessageDialog(this, errorMessage);

            }         

}
            


