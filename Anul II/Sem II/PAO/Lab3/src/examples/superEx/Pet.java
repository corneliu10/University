package examples.superEx;

public class Pet extends Animal{
    public Pet() {
//        super();
        System.out.println("This is the default Pet constructor");
    }

    public void showMessage(){
        System.out.println("This is a message from Pet class");
    }

    public void displayAMessage(){
        this.showMessage();
        super.showMessage();
    }
}
