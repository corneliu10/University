package tasks.task1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Date;

public class Main {
    public static void main(String[] args) {
        ReadWriteService rwInstance = ReadWriteService.getInstance();
        String dirPath = "C:\\Users\\corneliu.dumitru\\Desktop\\University\\Lab7\\src\\tasks\\task1\\data\\";

        User user = new User("Coco", new Date(1998,6,14), "1234");
        String userFileName = "user.txt";

        Item item1 = new Item("iphone", "XS", 1000.0);
        Item item2 = new Item("samsung", "S10", 800.0);
        String[] itemsFileName = {"item1.txt", "item2.txt"};

        Invoice invoice = new Invoice("123", new Date());
        String invoiceFileName = "invoice.txt";

        if (Files.notExists(Paths.get(dirPath))) {
            try {
                Files.createDirectory(Paths.get(dirPath));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        rwInstance.WriteObject(user, dirPath + userFileName);
        rwInstance.WriteObject(item1, dirPath + itemsFileName[0]);
        rwInstance.WriteObject(item2, dirPath + itemsFileName[1]);
        rwInstance.WriteObject(invoice, dirPath + invoiceFileName);

        System.out.println((User)rwInstance.ReadObject(dirPath + userFileName));
        System.out.println((Item)rwInstance.ReadObject(dirPath + itemsFileName[0]));
        System.out.println((Item)rwInstance.ReadObject(dirPath + itemsFileName[1]));
        System.out.println((Invoice)rwInstance.ReadObject(dirPath + invoiceFileName));
    }
}
