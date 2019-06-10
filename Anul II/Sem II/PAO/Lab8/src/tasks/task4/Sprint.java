package tasks.task4;

public class Sprint {
    private int days;
    private int hoursPerDay;

    public Sprint(int days, int hoursPerDay) {
        this.days = days;
        this.hoursPerDay = hoursPerDay;
    }

    public int getDays() {
        return days;
    }

    public int getHoursPerDay() {
        return hoursPerDay;
    }
}
