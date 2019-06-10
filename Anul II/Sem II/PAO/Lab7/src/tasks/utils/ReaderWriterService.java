package tasks.utils;

import tasks.exceptions.ReadLaboratorException;
import tasks.exceptions.WriteLaboratorException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ReaderWriterService {
    private static ReaderWriterService instance = new ReaderWriterService();

    private ReaderWriterService() {}

    public static ReaderWriterService getInstance() {
        return instance;
    }

    public void writeTextToFile(String fileNamePath, String text) throws WriteLaboratorException {
        FileWriter fw = null;
        try {
            fw = new FileWriter(fileNamePath);
            fw.write(text);
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (text.equals("alandala")) {
            throw new WriteLaboratorException();
        }

    }

    public String readTextFromFile(String fileNamePath, String text) throws ReadLaboratorException {
        FileReader fr = null;
        char[] textRead = new char[256];

        try {
            fr = new FileReader(fileNamePath);
            int len = fr.read(textRead);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : textRead) {
            sb.append(ch);
        }

        if (sb.indexOf(text) == -1)
            throw new ReadLaboratorException();
        else
            return sb.toString();
    }
}
