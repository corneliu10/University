package tasks.task3;

import tasks.task1.Pair;

public class Facebook {
    public static <T extends Employee> void printBuddies(Pair<T> buddies) {
        System.out.println(buddies.getFirst().getName() + " and " + buddies.getSecond().getName() + " are buddies!");
    }
}
