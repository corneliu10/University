package examples.absClasses;

public class Hipo extends Animal{
    public Hipo(int age){
        super(age);
    }
    public void printFunnyAge(){
        System.out.println(" The hipo has " + this.age + " years old");
    }

}
