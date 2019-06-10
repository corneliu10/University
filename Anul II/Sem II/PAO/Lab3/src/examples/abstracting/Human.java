package examples.abstracting;

public abstract class Human implements Activities {

    public void eat(){
        System.out.println("Humans eats food");
    }
    public void sleep(){
        System.out.println("Humans eats food");
    }

    public abstract void drink();

    public void move(){
        System.out.println("A human can move");
    }
}

