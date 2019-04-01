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
        return (double) 0;
    }

    @Override
    public Double getPerimeter() {
        return (double)0;
    }
}
