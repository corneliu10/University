package tasks.task3;

import tasks.task1.Pair;

public class Main {
    public static void main(String[] args) {
        Manager manager = new Manager("Boss", 999.00);
        Employee employee = new Employee("Corporatist", 0.1);
        Facebook.printBuddies(new Pair<Employee>(manager, employee));
    }
}
