package tasks.task4;

public class Main {
    public static void main(String args[])
    {
        Shape s1 = new Shape("John", "green");
        System.out.println(Shape.counter);

        Shape s2 = new Shape("Emma", "red");
        System.out.println(Shape.counter);

        Shape s3 = new Shape("Rick", "gray");
        System.out.println(Shape.counter);

        Shape[] shapes = { s1, s2, s3};

        for (Shape shape : shapes)
            shape.print();
    }
}
