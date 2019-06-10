package tasks.task8;

public class Main {
    public static void main(String[] args) {
        String str = "Subscribe to Pewdiepie";
        System.out.println(str.length());
        System.out.println(str.concat(" fast!"));
        System.out.println(str.toUpperCase());

        StringBuilder strBuilder = new StringBuilder(str);
        System.out.println(strBuilder.insert(9, " now"));
        strBuilder.replace(0, 10, "Unsubscribe ");
        strBuilder.replace(strBuilder.length() - 9, strBuilder.length(), "TSeries");
        System.out.println(strBuilder.toString());
        System.out.println(strBuilder.delete(12, 16));
        System.out.println(strBuilder.reverse());

        StringBuffer strBuffer = new StringBuffer(str);
        System.out.println(strBuffer.append(" and Julien"));
        System.out.println(strBuffer.reverse());
    }
}
