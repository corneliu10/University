package tasks.task4;

public class Shape {
    public static int counter = 5;

    public String name, color;

    public Shape(String name, String color)
    {
        counter++;
        this.name = name;
        this.color = color;
    }

    public void print()
    {
        System.out.println("Name: " + name + " Color: " + color);
    }
}
