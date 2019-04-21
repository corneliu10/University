package tasks.task1;

public class Main {
    public static void main(String args[]) {
        Pair<String> stringPair = new Pair<String>("abc", "efg");
        Pair<Number> numberPair = new Pair<Number>(123, 456);

        System.out.println(stringPair.toString());
        System.out.println(numberPair.toString());
    }
}
