package examples.exceptionsEx;

public class UncheckedExceptionsExample {

    public static void catchRuntimeEx() {
//         throwExplicitRuntimeEx();
        try {
            throwRuntimeEx();
        } catch (RuntimeException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public static void throwRuntimeEx() {
        throw new RuntimeException("No throws clause necessary!");
    }

    public static void throwExplicitRuntimeEx() throws RuntimeException {
        throw new RuntimeException("I added throws clause because I want to!");
    }

    public static void main(String[] args) {
        catchRuntimeEx();
    }
}
