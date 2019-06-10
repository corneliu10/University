package examples.accessModifiers.package2;

/**
 * Created by bogdan pahontu
 */
public class AccessExample {

    public static void main(String args[]){
        AccessExample.printPrivate();
    }

    public static void printPublic(){
        System.out.println("This is a public method");
    }

     static void printDefault(){
        System.out.println("This is a default method");
    }

    private static void printPrivate(){
        System.out.println("This is a private method");
    }

    protected static void printProtected(){
        System.out.println("This is a protected method");
    }
}
