package examples.overREx;

public class Eagle extends Bird {

    // Overload example
    public int fly(int height) {
        System.out.println("Bird is flying at " + height + " meters");
        return height;
    }

    @Override
    public void eat(int food) {

        System.out.println("Eagle is eating " + food + " units of food");
    }

//    @Override
//    private void eat(int food) {
//
//        System.out.println("Eagle is eating " + food + " units of food");
//    }


//    public int eat(int food) { // DOES NOT COMPILE
//        System.out.println("Bird is eating " + food + " units of food");
//        return food;
//    }

}
