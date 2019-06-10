package tasks.task1;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ReadWriteService {
    private static ReadWriteService instance = new ReadWriteService();
    private List<String> objectTypes;

    private ReadWriteService() {
        objectTypes = new ArrayList<>();
        objectTypes.add("Invoice");
        objectTypes.add("Item");
        objectTypes.add("User");
    }

    public static ReadWriteService getInstance() {
        return instance;
    }

    public boolean WriteObject(Object obj, String filePath) {
        boolean ok = false;
        for (String type : objectTypes) {
            if (type.equals(obj.getClass().getSimpleName())) {
                ok = true;
            }
        }
        if (!ok) return false;

        try {
            FileOutputStream fileOut = new FileOutputStream(filePath);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(obj);
            out.close();
            fileOut.close();
            System.out.println("Serialized object is saved in " + filePath);
            return true;
        } catch (IOException ex) {
            ex.printStackTrace();
            return false;
        }
    }

    public Object ReadObject(String filePath) {
        Object obj = null;
        try {
            FileInputStream fileIn = new FileInputStream(filePath);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            obj = in.readObject();
            in.close();
            fileIn.close();

        } catch (IOException | ClassNotFoundException ex) {
            ex.printStackTrace();
        }

        return obj;
    }
}
