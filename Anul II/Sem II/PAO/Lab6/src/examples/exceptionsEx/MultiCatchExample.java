package examples.exceptionsEx;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;

public class MultiCatchExample {
    public static void oldSchoolCatches() {
        try {
            Path path = Paths.get("dolphinsBorn.txt");
            String text = new String(Files.readAllBytes(path));
            LocalDate date = LocalDate.parse(text);
            System.out.println(date);
        } catch (DateTimeParseException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    public static void badGeneralExceptionCatch() {
        try {
            Path path = Paths.get("dolphinsBorn.txt");
            String text = new String(Files.readAllBytes(path));
            LocalDate date = LocalDate.parse(text);
            System.out.println(date);
        } catch (Exception e) { // BAD approach
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    public static void decentCatches() {
        try {
            Path path = Paths.get("dolphinsBorn.txt");
            String text = new String(Files.readAllBytes(path));
            LocalDate date = LocalDate.parse(text);
            System.out.println(date);
        } catch (DateTimeParseException e) {
            handleException(e);
        } catch (IOException e) {
            handleException(e);
        }
    }

    private static void handleException(Exception e) {
        e.printStackTrace();
        throw new RuntimeException(e);
    }

    public static void multiCatches() {
        try {
            Path path = Paths.get("dolphinsBorn.txt");
            String text = new String(Files.readAllBytes(path));
            LocalDate date = LocalDate.parse(text);
            System.out.println(date);
            // } catch (DateTimeParseException | FileNotFoundException | -- THis is not right because FileNotFoundException extends IOException
            // IOException e) {
        } catch (DateTimeParseException | IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }


    public static void main(String[] args) {
        // oldSchoolCatches();
        // badGeneralExceptionCatch();
        // decentCatches();
         multiCatches();
    }
}
