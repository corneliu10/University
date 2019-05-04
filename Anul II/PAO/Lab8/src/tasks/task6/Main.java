package tasks.task6;

import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> wordsFreq = ParseFile.extractWordsFrequency("./src/tasks/task6/data.txt");

        for(Map.Entry<String, Integer> entry : wordsFreq.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();

            System.out.println(key + " : " + value);
        }
    }
}
