package examples.staticExamples;

/**
 * Created by bpahontu on 3/4/2019.
 */
public class ExMessage {

    String message;
    static String staticMessage = "Default message";

    public static void main(String[] args){
        printMessageStatic();
    }

    public ExMessage(String message) {
        this.message = message;
    }

    public static void printMessageStatic(){
//        Not working
//        System.out.println(message);
//        System.out.println(this.message);

        System.out.println(staticMessage);
        ExMessage em = new ExMessage("First message");
        System.out.println(em.message);
    };

    public void printMessage(){
        System.out.println(this.message);
    }
}
