package examples.constructors;

/**
 * Created by bogdan pahontu
 */
public class Main {
    public static void main(String args[]){
        Person p1 = new Person("John", 23);
        p1.printPerson();

        Person p2 = new Person();
        p2.setName("Ian");
        p2.setAge(33);
        p2.printPerson();

        Animal a1 = new Animal();
        a1.setName("Dog");
        a1.setType("domestic");
        a1.printAnimal();

    }
}
