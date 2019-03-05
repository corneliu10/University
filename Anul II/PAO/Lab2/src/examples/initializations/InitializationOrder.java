package examples.initializations;

/**
 * Created by bogdan pahontu
 */
public class InitializationOrder {

    private String name = "Torchie";

    { System.out.println(name); }

    private static int COUNT = 0;

    static { System.out.println(COUNT); }

    static { COUNT += 10;
        System.out.println(COUNT);
    }

    public InitializationOrder() {
        System.out.println("constructor");
    }
}
