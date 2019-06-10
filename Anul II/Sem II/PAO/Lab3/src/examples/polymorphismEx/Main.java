package examples.polymorphismEx;

public class Main {
    public static void main(String[] args){
        Animal animal = new Animal();
        animal.makeSound();

        Animal dog = new Dog();
        dog.makeSound();

        Animal cat = new Cat();
        cat.makeSound();
    }
}
