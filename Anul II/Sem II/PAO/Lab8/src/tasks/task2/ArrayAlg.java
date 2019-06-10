package tasks.task2;

import tasks.task1.Pair;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ArrayAlg {
    public static <T extends Comparable<T>> Pair<T> minMax(List<T> objs) {
        if (objs.size() == 0)
            return null;

        Collections.sort(objs);
        return new Pair<T>(objs.get(0), objs.get(objs.size()-1));
    }
}
