package tasks.shapeDemo;

public class Rectangle implements Shape {
    private Double sideA;
    private Double sideB;

    public Rectangle(Double sideA, Double sideB) {
        this.sideA = sideA;
        this.sideB = sideB;
    }

    @Override
    public Double getArea() {
        return (double) (sideA * sideB);
    }

    @Override
    public Double getPerimeter() {
        return (double) (2 * sideA + 2 * sideB);
    }
}
