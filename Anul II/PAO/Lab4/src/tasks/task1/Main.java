package tasks.task1;

public class Main {
    public static void main(String[] args) {
        String str = "Subscribe to Pewdiepie!";

        System.out.println(str.indexOf("P"));
        System.out.println(str.lastIndexOf("e"));
        System.out.println(str.length());

        String[] strArray = str.split(" ");
        for (String s : strArray) {
            System.out.println(s);
        }
    }
}
