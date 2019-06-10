package tasks.task6;

public class Main {
    public static void main(String[] args) {
        Configuration productConfig = new Configuration("localhost/release", "C://Release", "IJ");
        Configuration developmentConfig = new Configuration("localhost/debug", "C://Debug", "IJ");
    }
}
