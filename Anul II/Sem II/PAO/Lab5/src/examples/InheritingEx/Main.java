package examples.InheritingEx;

public class Main {

    public static void main(String args[]){
        Furniture f = new Furniture(20,30,10);
        System.out.println(f.getPropertyName());
        System.out.println(f.getDepth());
        System.out.println(f.getHeight());
        System.out.println(f.getWidth());
    }
}
