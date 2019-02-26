package examples;

/**
 * Created by bogdan pahontu
 */
public class K_Operators {
    public static void main(String args[]){
        boolean x = false;
        System.out.println(x);
        x = !x;
        System.out.println(x);
//        int x2 = !5;
        double x3 = 1.21;
        System.out.println(x3);
        x3 = -x3;
        System.out.println(x3);
        x3 = -x3;
        System.out.println(x);
//        boolean y = -true;
//        boolean z = !0;

        int x5 = 3;
        int y5 = ++x5 * 5 / x5-- + --x5;
        System.out.println("x5 is " + x5);
        System.out.println("y5 is " + y5);
//        int x7 = 1.0;
//        short y7 = 1921222;
//        int z7 = 9f;
//        long t7 = 192301398193810323;
        int x8 = (int)1.0;
        short y8 = (short)1921222;
        int z8 = (int)9l;
        long t8 = 192301398193810323l;


    }
}
