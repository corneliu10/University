package examples.theObject;

public class Main {
    public static void main(String args[]){
        MyCustomObject obj = new MyCustomObject();
        System.out.println(obj.toString());
        Class c = obj.getClass();
        System.out.println(c.getName());
    }
}
