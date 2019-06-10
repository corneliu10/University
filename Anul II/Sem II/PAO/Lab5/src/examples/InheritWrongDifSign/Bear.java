package examples.InheritWrongDifSign;

//public class Bear implements Herbivore, Omnivore {
public class Bear{
    public int eatPlants() { //DOES NOT COMPILE
        System.out.println("Eating plants: ");
        return 2;
    }

//    public String eatPlants() {//DOES NOT COMPILE
//        System.out.println("Eating plants");
//        return "test";
//    }

}
