package tasks.utils;

import tasks.exceptions.ReadLaboratorException;
import tasks.exceptions.WriteLaboratorException;

public class Main {
    public static void main(String[] args) {
        ReaderWriterService rws = ReaderWriterService.getInstance();
        String filePath = ".\\src\\tasks\\utils\\test.txt";

        try {
            rws.writeTextToFile(filePath,"alandala");
        } catch (WriteLaboratorException e) {
            System.out.println(e.getName());
        }

        try {
            System.out.println(rws.readTextFromFile(filePath, "alandaladd"));
        } catch (ReadLaboratorException e) {
            System.out.println(e.getName());
        }
    }
}
