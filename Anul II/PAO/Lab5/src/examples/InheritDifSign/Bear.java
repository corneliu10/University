package examples.InheritDifSign;

public class Bear implements Herbivore, Omnivore {
    public int eatPlants(int quantity) {
        System.out.println("Eating plants: " + quantity);
        return quantity;
    }

    public void eatPlants() {
        System.out.println("Eating plants");
    }

    public static void main(String args[]){
        Bear b = new Bear();
        System.out.println(Herbivore.CUSTOM_MAX);
        System.out.println(Omnivore.CUSTOM_MAX);
    }

}
