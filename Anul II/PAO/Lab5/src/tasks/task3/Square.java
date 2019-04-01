package tasks.task3;

public class Square implements Enclosure {
    double width;

    public Square(double width) {
        this.width = width;
    }

    @Override
    public double perimeter() {
        return 4 * width;
    }

    @Override
    public double area() {
        return width * width;
    }
}
