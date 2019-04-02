package examples.exceptionsEx;

public class ErrorTypesExamples {
//     ExceptionInInitializerError
     static {
     int[] countsOfMoose = new int[3];
     int num = countsOfMoose[-1];
     }

    // StackOverflowError
    public static void doNotCodeThis(int num) {
        doNotCodeThis(1);
    }

    // NoClassDefFoundError -> complex, not needed

    public static void main(String[] args) {
        // doNotCodeThis(10);
    }
}
