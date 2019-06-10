package lab1.tasks.task2;

public class ZooArguments {
    public static void main(String args[])
    {
        switch (args.length) {
            case 0:
                System.out.println("No arguments provided!");
                break;
            case 1:
                System.out.println("One argument: " + args[0]);
                break;
            case 2:
                System.out.println("Two arguments: " + args[0] + " " + args[1]);
                break;
            case 3:
                System.out.println("Three arguments: " + args[0] + " " + args[1] + " " + args[2]);
                break;
            default:
                System.out.println("More than 3 arguments provided!");
                break;
        }
    }
}
