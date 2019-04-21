package examples.eSet;

import java.util.TreeSet;

public class TreeSetExample {
    public static void main(String[] args)
    {
        TreeSet<String> ts1 = new TreeSet<String>();

        // Elements are added using add() method
        ts1.add("A");
        ts1.add("B");
        ts1.add("C");

        // Duplicates will not get insert
        ts1.add("C");

        // Elements get stored in default natural
        // Sorting Order(Ascending)
        System.out.println(ts1);

        TreeSet<StringBuffer> ts = new TreeSet<StringBuffer>();

        // Elements are added using add() method
        ts.add(new StringBuffer("A"));
        ts.add(new StringBuffer("Z"));
        ts.add(new StringBuffer("L"));
        ts.add(new StringBuffer("B"));
        ts.add(new StringBuffer("O"));

        // We will get RunTimeException :ClassCastException
        // As StringBuffer does not implements Comparable interface
        System.out.println(ts);
    }
}
