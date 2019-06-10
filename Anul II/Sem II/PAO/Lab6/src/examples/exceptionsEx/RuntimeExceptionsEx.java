package examples.exceptionsEx;

public class RuntimeExceptionsEx {
    private static String name;

    public static void runtimeExceptions() {


//         ArithmeticException
         int answer = 11 / 0;

//         ArrayIndexOutOfBoundsException
         int[] countsOfMoose = new int[3];
         System.out.println(countsOfMoose[-1]);

//         ClassCastException
         String type = "moose";
         Object obj = type;
         Integer number = (Integer) obj;

//         IllegalArgumentException
         printPositiveNumber(-1);

//         NullPointerException
         System.out.println(name.length());

//         NumberFormatException
         Integer.parseInt("abc");
    }

    public static void printPositiveNumber(int number) {
        if (number < 0) {
            throw new IllegalArgumentException("number must not be negative");
        }
        System.out.println(number);
    }

    public static void main(String[] args) {
        runtimeExceptions();
    }
}
