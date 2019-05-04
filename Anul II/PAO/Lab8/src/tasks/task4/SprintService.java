package tasks.task4;

import java.util.*;

public class SprintService {
    private static SprintService instance = new SprintService();
    private Sprint sprint;

    private SprintService() {
        sprint = new Sprint(10, 8);
    }

    public static SprintService getInstance() {
        return instance;
    }

    public Map<Employee, List<Task>> solveSprint(HashSet<Employee> employees,
                                                 PriorityQueue<Task> tasks) {
        int totalHours = sprint.getHoursPerDay() * sprint.getDays();
        double totalMinutes = totalHours * 60;
        int employeePick = 0; double maxTime;

        Map<Employee, List<Task>> sprintSolved = new HashMap<>();

        while (!tasks.isEmpty()) {
            Task t = tasks.poll();
            if (t.getTime() > totalMinutes) {
                System.out.println("Didn't solved all tasks");
                break;
            }
        }

        return sprintSolved;
    }
}
