package tasks.task5;

import java.util.List;
import java.util.Map;

import static tasks.task6.ParseFile.readFromFile;

public class Main {
    public static void main(String[] args) {
        String str = readFromFile("./src/tasks/task5/data.txt").get(0);
        Map<WordType, List<String>> words = StringSeparator.separateString(str);

        for (WordType word : words.keySet()) {
            System.out.print(word + " : ");
            printList(words.get(word));
        }
    }

    public static <T> void printList(List<T> list) {
        for (T item : list) {
            System.out.print(item + " ");
        }

        System.out.println();
    }
}
