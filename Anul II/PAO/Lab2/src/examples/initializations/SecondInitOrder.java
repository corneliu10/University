package examples.initializations;

/**
 * Created by bpahontu on 3/4/2019.
 */
public class SecondInitOrder {
    private String name = "Torchie";

    public SecondInitOrder() {
        System.out.println("constructor");

    }

    {System.out.println(name);}

    private static int COUNT = 0;

    static {
        System.out.println(COUNT);
//        System.out.println(this.name);
    }

    {
        COUNT++;
        System.out.println(COUNT);
    }



    public static void main(String args[]){
        System.out.println("read to construct");
        new SecondInitOrder();
    }
}
