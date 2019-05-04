package tasks.task4;

enum Grade {
    Junior(1.25),
    Technician(1.00),
    Engineer(0.75);

    private double grade;

    Grade(double grade) {
        this.grade = grade;
    }

    public double getGrade() {
        return grade;
    }
}

public class Employee implements Comparable<Employee> {
    private String name;
    private Grade grade;

    public Employee() {
    }

    public Employee(String name, Grade grade) {
        this.name = name;
        this.grade = grade;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Grade getGrade() {
        return grade;
    }

    public void setGrade(Grade grade) {
        this.grade = grade;
    }

    @Override
    public int compareTo(Employee o) {
        if (o.grade.getGrade() > this.grade.getGrade())
            return -1;
        else if (o.grade.getGrade() < this.grade.getGrade())
            return 1;

        return 0;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", grade=" + grade +
                '}';
    }
}
