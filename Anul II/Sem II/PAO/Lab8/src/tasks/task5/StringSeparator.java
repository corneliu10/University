package tasks.task5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StringSeparator {
    public static Map<WordType, List<String>> separateString(String str) {
        String[] words = str.split("\\s+");
        Map<WordType, List<String>> wordsMap = new HashMap<>();
        wordsMap.put(WordType.Alpha, new ArrayList<>());
        wordsMap.put(WordType.Numerics, new ArrayList<>());
        wordsMap.put(WordType.AlphaNumerics, new ArrayList<>());
        wordsMap.put(WordType.Other, new ArrayList<>());

        for (String word : words) {
            if (containsSpecialKeys(word)) {
                wordsMap.get(WordType.Other).add(word);
            } else if (containsAlpha(word) && containsNumeric(word)) {
                wordsMap.get(WordType.AlphaNumerics).add(word);
            } else if (containsAlpha(word)) {
                wordsMap.get(WordType.Alpha).add(word);
            } else if (containsNumeric(word)) {
                wordsMap.get(WordType.Numerics).add(word);
            }
        }

        return wordsMap;
    }

    private static boolean containsAlpha(String str) {
        for (int i = 0; i < str.length(); ++i) {
            if (Character.isLetter(str.charAt(i)))
                return true;
        }

        return false;
    }

    private static boolean containsNumeric(String str) {
        for (int i = 0; i < str.length(); ++i) {
            if (Character.isDigit(str.charAt(i)))
                return true;
        }

        return false;
    }

    private static boolean containsSpecialKeys(String str) {
        for (int i = 0; i < str.length(); ++i) {
            if (!Character.isDigit(str.charAt(i)) && !Character.isLetter(str.charAt(i)))
                return true;
        }

        return false;
    }
}
