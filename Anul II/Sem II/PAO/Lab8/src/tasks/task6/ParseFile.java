package tasks.task6;

import tasks.task5.StringSeparator;
import tasks.task5.WordType;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParseFile {
    public static List<String> readFromFile(String fileName) {
        List<String> lines = new ArrayList<>();
        String line = null;

        try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader =
                    new FileReader(fileName);

            BufferedReader bufferedReader =
                    new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                lines.add(line);
            }

            bufferedReader.close();
        } catch(FileNotFoundException ex) {
            System.out.println(
                    "Unable to open file '" +
                            fileName + "'");
        } catch(IOException ex) {
            System.out.println(
                    "Error reading file '"
                            + fileName + "'");
            // Or we could just do this:
            // ex.printStackTrace();
        }

        return lines;
    }

    public static Map<String, Integer> extractWordsFrequency(String fileName) {
        return extractWordsFrequency(fileName, false);
    }

    public static Map<String, Integer> extractWordsFrequency(String fileName, boolean caseSensitive) {
        List<String> lines = readFromFile(fileName);
        Map<String, Integer> wordsFrequency = new HashMap<>();

        for (String line : lines) {
            Map<WordType, List<String>> wordsType = StringSeparator.separateString(line);

            for (String word : wordsType.get(WordType.Alpha)) {
                if (!caseSensitive) word = word.toLowerCase();
                if (!wordsFrequency.containsKey(word)) {
                    wordsFrequency.putIfAbsent(word, 1);
                } else {
                    wordsFrequency.put(word, wordsFrequency.get(word) + 1);
                }
            }
        }

        return wordsFrequency;
    }
}
