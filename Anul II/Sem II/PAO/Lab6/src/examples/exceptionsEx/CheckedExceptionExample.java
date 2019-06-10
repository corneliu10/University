package examples.exceptionsEx;

import examples.exceptionsEx.custom.SimpleCheckedException;

public class CheckedExceptionExample {
    public static void catchCheckedEx() {
        // throwCheckedEx();
        try {
            throwCheckedEx();
        } catch (SimpleCheckedException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public static void throwCheckedEx()  throws SimpleCheckedException {
        throw new SimpleCheckedException("I was forced to add the throws clause necessary!");
    }

    public static void main(String[] args) {
        catchCheckedEx();
    }
}
