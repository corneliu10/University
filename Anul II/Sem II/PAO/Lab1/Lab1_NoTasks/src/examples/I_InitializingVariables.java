package examples;

/**
 * Created by bogdan pahontu
 */
public class I_InitializingVariables {
    public static void main(String args[]){
        I_InitializingVariables myObj = new I_InitializingVariables();

        System.out.println(myObj.notValid());

        myObj.findAnswer(true);
        myObj.findAnswer(false);
    }

    public int notValid() {
        int y = 10;
        int x;
        //int reply = x + y; // DOES NOT COMPILE
        //return reply;
        return 0;
    }

    public void findAnswer(boolean check) {
        int answer;
        int onlyOneBranch;
        if (check) {
            onlyOneBranch = 1;
            answer = 1;
        } else {
            answer = 2;
        }
        System.out.println(answer);
        // compiler knows there is a possibility for check to be false leaving onlyOneBranch uninitialized
//        System.out.println(onlyOneBranch);
    }

    public void initializationVariables(){
        String a; int b;
//        a=”test”; b=8;
        String s3 = "yes", s4 = "no";
        int i1, i2, i3 = 0;
//        int num, String value; // DOES NOT COMPILE

        boolean b1, b2;
        String s1 = "1", s2;
//        double d1, double d2;
//        int i1; int i2;
//        int i3; i4;

    }
}
