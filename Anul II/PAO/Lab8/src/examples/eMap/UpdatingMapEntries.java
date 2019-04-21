package examples.eMap;

import java.util.HashMap;
import java.util.Map;

public class UpdatingMapEntries {
    public static void main(String args[]){
        Map<String,Integer> counts = new HashMap<String,Integer>();
        String word = "string1";

        // First time this returns a NullPointerException
//        counts.put(word, counts.get(word) + 1);

        // Good Example
//        counts.put(word, counts.getOrDefault(word, 0) + 1);

        // Second approach: putIfAbsent method
        counts.putIfAbsent(word, 0);
        counts.put(word, counts.get(word) + 1);

        // Third approach: merge method
        counts.merge(word, 1, Integer::sum);


        for(Map.Entry<String,Integer> entry:counts.entrySet()){
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
