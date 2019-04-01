package tasks.shapeDemo;

import javax.naming.Name;

public class Main {
    public static void main(String[] args) {
        Shape rectangle = new Rectangle(10.0, 15.0);
        Shape triangle = new Triangle(2.0,3.0 , 5.0);
        System.out.println(rectangle.getArea());
        System.out.println(rectangle.getPerimeter());
        System.out.println();
        System.out.println(triangle.getArea());
        System.out.println(triangle.getPerimeter());

        Shape square = new Square(10.0);
        System.out.println(square.getArea());
        System.out.println(square.getPerimeter());

        NamedObject customTriangle = new CustomTriangle(2.0,3.0 , 5.0);
        System.out.println(customTriangle.getName());
        System.out.println(customTriangle.getDescription());
    }
}
