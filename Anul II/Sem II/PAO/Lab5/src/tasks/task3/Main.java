package tasks.task3;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Enclosure> objs = new ArrayList<Enclosure>();

        objs.add(new Circle(10));
        objs.add(new Square(10));

        System.out.println(objs.get(0).perimeter());
        System.out.println(objs.get(0).area());
        System.out.println();
        System.out.println(objs.get(1).perimeter());
        System.out.println(objs.get(1).area());
    }
}