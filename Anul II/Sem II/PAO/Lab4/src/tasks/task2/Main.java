package tasks.task2;

public class Main {
    public static void main(String[] args) {
        String str = "   dsf fd  ";

        System.out.println(removeLeadingSpaces(str));
    }

    public static String removeLeadingSpaces(String str) {
        return str.trim();
    }
}
