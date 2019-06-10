package tasks.task7;



public class Main {
    static final int NCHARS = 256;

    public static void main(String[] args) {
        String str = new String("succcesses");

        System.out.println(secondMostFrequent(str));
    }

    public static char secondMostFrequent(String str) {
        if (str.isEmpty()) return ' ';
        int[] freq = new int[NCHARS];

        for(int i = 0; i < str.length(); ++i) {
            freq[(int)str.charAt(i)]++;
        }

        int maxChar = 0, secondMaxChar = 0;
        for (int i = 0; i < NCHARS; ++i) {
            if (freq[i] > freq[maxChar]) {
                secondMaxChar = maxChar;
                maxChar = i;
            }
            else if (freq[i] < freq[maxChar] &&
                     freq[i] > freq[secondMaxChar]) {
                secondMaxChar = i;
            }
        }

        return (char)secondMaxChar;
    }
}
