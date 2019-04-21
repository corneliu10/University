package examples.generics;

public class BoundExample {
    public static void main(String a[])
    {
        //Creating object of sub class A and
        //passing it to Bound as a type parameter.
        Bound<A> bea = new Bound<A>(new A());
        bea.doRunTest();

    }
}

// We should ha single class(A)
class Bound<T extends A & B>
{

    private T objRef;

    public Bound(T obj){
        this.objRef = obj;
    }

    public void doRunTest(){
        this.objRef.displayClass();
    }
}

interface B
{
    public void displayClass();
}

class A implements B
{
    public void displayClass()
    {
        System.out.println("Inside super class A");
    }
}
