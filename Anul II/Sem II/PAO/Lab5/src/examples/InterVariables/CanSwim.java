package examples.InterVariables;

public interface CanSwim {
    int maxDepth = 100;
    final static boolean underwater = true;
    public static final String defaultName = "fish";

//    private int prvMaxDepth = 200; // DOES NOT COMPILE
//    protected abstract int anotherVariable = 10; // DOES NOT COMPILE
}
