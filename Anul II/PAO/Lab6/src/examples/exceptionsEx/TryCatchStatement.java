package examples.exceptionsEx;

public class TryCatchStatement {
    public static void explore() {
        System.out.println("walking");
        // try removing curly braces or blocks
        // try changing the exception in fall() to a checked exception
        try {
            fall();
            System.out.println("never get here");
        } catch (RuntimeException e) {
            System.out.println(e.getMessage());
            cry();
        } finally {
            getUp();
        }
        seeAnimals();
    }

    public static void fall() {
        throw new RuntimeException("falling exception");
    }

    public static void cry() {
        System.out.println("wuaaaaaaaa!!!!");
    }

    public static void getUp() {
        System.out.println("getting up");
    }

    public static void seeAnimals() {
        System.out.println("seeing animals");
    }

    public static void killFinally() {
        String s = "";
        try {
            s += "t";
        } catch (Exception e) {
            s += "c";
        } finally {
             System.exit(0);
            s += "f";
        }
        s += "a";
        System.out.print(s);
    }

    public static void main(String[] args) {
//         explore();
         killFinally();
    }

}
