package tasks.task2;

import java.io.EOFException;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;

public class RAFService {
    private static RAFService instance = new RAFService();

    private RAFService() {}

    public static RAFService getInstance() {
        return instance;
    }

    public void write(Object obj, String filePath) throws IOException {
        RandomAccessFile raf = new RandomAccessFile(filePath, "w");

        StringBuilder sb = new StringBuilder();
        if (obj != null) {
            sb.append(obj.toString());
        }

        raf.writeChars(sb.toString());
        raf.close();
    }


    public String read(String filePath) throws IOException {
        RandomAccessFile raf = new RandomAccessFile(filePath, "w");

        StringBuilder sb = new StringBuilder();
        while (true) {
            try {
                sb.append(raf.readChar());
            } catch (EOFException e) {
                break;
            }
        }

        raf.close();
        return sb.toString();
    }
}
