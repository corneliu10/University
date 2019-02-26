package examples;

/**
 * Created by bogdan pahontu
 */
public class F_PrimitivesVsReferences {
    //this will have the default value of a reference type
    public Object myObj;

    //int i = null; // compile time error -- can't set a null value to a primitive

    public static void main(String[] args) {

        //long max = 3123456789; // DOES NOT COMPILE
        long max = 3123456789L; // now Java knows it is a long
        System.out.println(max);

        // Since JAVA 7
        long creditCardNb = 1234_5678_9101_123L;

        F_PrimitivesVsReferences instance = new F_PrimitivesVsReferences();
        System.out.println("What is value of myObjc : " + instance.myObj);

        String reference = "hello";
        int len = reference.length();
        System.out.println(len);
        //int bad = len.length(); // compile error -- there are no methods on primitives

//        Integer itr = null; // this is ok
//        int j = itr; // this is also ok?
    }

    public static void boxUnbox(){
        // Unboxing
        Integer obj = new Integer("2526");
        int i = obj.intValue();
        System.out.println(i);


        // Boxing
        int j = 2;
        Integer k = new Integer(j);
        System.out.println(k);
    }
}
