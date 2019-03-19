package tasks.task3;

public class Main {
    public static void main(String[] args) {
        String str1 = "Elena ";
        String str2 = "bea cafele";

        System.out.println(concatenateStrings(str1, str2));
    }

    public static String concatenateStrings(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        String sL1 = s1.toLowerCase(), sL2 = s2.toLowerCase();
        if (sL1.substring(0, 3).equals(sL2.substring(len2 - 3, len2))) {
            return s1.concat(s2);
        };

        return "";
    }
}
