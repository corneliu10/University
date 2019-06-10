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
        return Math.sqrt(getPerimeter()/2 * (getPerimeter()/2 - sideA) *
                        (getPerimeter()/2 - sideB) * (getPerimeter()/2 - sideC));
    }

    @Override
    public Double getPerimeter() {
        return sideA + sideB + sideC;
    }
}
