package examples.immutableEx;

public class Main {
    public static void main(String args[]) {
        ImmutableExample ie = new ImmutableExample("IE1", 10);
        System.out.println(ie.getName());
        System.out.println(ie.getRegNo());
    }
}
