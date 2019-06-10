package tasks.task3;

import java.io.*;
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        writeProperties(".\\config.properties");
        printProperties(".\\config.properties");
    }

    public static void writeProperties(String fileName) {
        try (OutputStream output = new FileOutputStream(fileName)) {
            Properties properties = new Properties();

            properties.setProperty("test", "123");
            properties.setProperty("SUBSCRIBE", "PEWDIEPIE");

            properties.store(output, null);

            System.out.println(properties);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void printProperties(String fileName) {
        Properties properties = new Properties();

        try {
            properties.load(new FileReader(new File(fileName)));

            for (String key : properties.stringPropertyNames()) {
                System.out.println(key + " : " + properties.getProperty(key));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
