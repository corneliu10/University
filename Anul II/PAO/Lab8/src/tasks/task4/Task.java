package tasks.task4;

enum Severity {
    Sev3,
    Sev2,
    Sev1
}

public class Task implements Comparable<Task> {
    private String name;
    private double time; // in min
    private Severity severity;
    private boolean backLog;

    public Task(String name, double time, Severity severity, boolean backLog) {
        this.name = name;
        this.time = time;
        this.severity = severity;
        this.backLog = backLog;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }

    public Severity getSeverity() {
        return severity;
    }

    public void setSeverity(Severity severity) {
        this.severity = severity;
    }

    public boolean isBackLog() {
        return backLog;
    }

    public void setBackLog(boolean backLog) {
        this.backLog = backLog;
    }

    @Override
    public int compareTo(Task o) {
        if (this.severity.ordinal() < o.severity.ordinal()) {
            return 1;
        } else if (this.severity.ordinal() > o.severity.ordinal()) {
            return -1;
        }

        return Boolean.compare(o.backLog, this.backLog);
    }

    @Override
    public String toString() {
        return "Task{" +
                "name='" + name + '\'' +
                ", time=" + time +
                ", severity=" + severity +
                ", backLog=" + backLog +
                '}';
    }
}
