public class MVCExercise {

    public static void main(String[] args) {  

            PriceView theView = new PriceView();

            PriceModel theModel = new PriceModel();

            PriceController theController = new PriceController(theView,theModel);

            theView.setVisible(true);      

    }

}
