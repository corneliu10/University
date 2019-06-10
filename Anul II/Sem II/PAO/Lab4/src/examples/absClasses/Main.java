package examples.absClasses;

public class Main {

    public static void main(String args[]){
        Hipo h = new Hipo(23);
        h.printFunnyAge();

        Hipo.printcount();

        Hipo h2 = new Hipo(12);
        h2.printFunnyAge();

        Hipo.printcount();

    }
}
