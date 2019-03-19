package examples.absClasses;

public abstract class Animal {
    protected int age;
    protected static int count;
    public final void eat(){
        System.out.println("Animal is eating");
    }

    // what happens if i`ll remove the static keyword ??
    static {
        count = 0;
    }

    public Animal(int age){
        this.age = age;
        count ++;
    }

    public abstract void printFunnyAge();

    public static void printcount(){
        System.out.println("Number of animals: " + count);
    }
}
