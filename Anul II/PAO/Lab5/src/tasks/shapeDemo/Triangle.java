package tasks.shapeDemo;

public class Triangle implements Shape {
    private Double sideA;
    private Double sideB;
    private Double sideC;

    public Triangle(Double sideA, Double sideB, Double sideC) {
        this.sideA = sideA;
        this.sideB = sideB;
        this.sideC = sideC;
    }

    @Override
    public Double getArea() {
        return null;
    }

    @Override
    public Double getPerimeter() {
        return null;
    }
}
