package tasks.shapeDemo;

public class CustomTriangle extends Triangle implements NamedObject {
    private String name;
    private String description;

    public CustomTriangle(Double sideA, Double sideB, Double sideC) {
        super(sideA, sideB, sideC);
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getDescription() {
        return description;
    }
}
