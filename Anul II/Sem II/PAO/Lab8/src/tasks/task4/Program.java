package tasks.task4;

import java.util.*;

public class Program {
    public static void main(String[] args) {
        Set<Employee> employees = new HashSet<>();
        employees.add(new Employee("Jon", Grade.Junior));
        employees.add(new Employee("Wick", Grade.Technician));
        employees.add(new Employee("Sarah", Grade.Engineer));

        PriorityQueue<Task> tasks = new PriorityQueue<>();
        tasks.add(new Task("1 feature", 120,  Severity.Sev1, true));
        tasks.add(new Task("2 feature", 170,  Severity.Sev3, false));
        tasks.add(new Task("3 feature", 150,  Severity.Sev1, false));
        tasks.add(new Task("1 bug", 50,  Severity.Sev2, true));

        Sprint sprint = new Sprint(10, 8);

        for (Employee e : employees) {
            System.out.println(e);
        }
    }
}
