package examples.lion;

public class Lion extends Animal {
    private void roar() {
        System.out.println("The " + getAge() + " year old lion says: Roar!");
    }

    // Why this will not compile ? What can we do in order to make it work?
    private void roar2() {
//        System.out.println("The "+ age +" year old lion says: Roar!");
    }

}
