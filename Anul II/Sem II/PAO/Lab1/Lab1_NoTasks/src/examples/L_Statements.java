package examples;

/**
 * Created by bogdan pahontu
 */
public class L_Statements {
    public static void main(String args[]){
        System.out.println("-------------------");
        ifStatement();

        System.out.println("-------------------");
        switchStatement(5);
        switchStatement(10);

        System.out.println("-------------------");
        whileStatement();
        doWhileStatement();

        System.out.println("-------------------");
        forStatement();

        System.out.println("");
        System.out.println("-------------------");
        forEachStatement();

        System.out.println("");
        System.out.println("-------------------");
        breakStatement();

        System.out.println("");
        System.out.println("-------------------");
        continueStatement();


    }

    public static void ifStatement(){
        int a = 20;
        int b = 10;
        int c = 30;

        if(a < b){
            System.out.println("b is greater then a");
        }else if( a > c){
            System.out.println("a is greater then c");
        }else{
            System.out.println("None of the first two conditions are true");
        }

        // Ternary operator
        System.out.println(a > b ? a : b);
    }

    public static void switchStatement(int number){
        switch(number){
            case 10:
                System.out.println("Number is 10");
                break;
            case 1:
                System.out.println("Number is 1");
                break;
            default:
                System.out.println("Other number");
        }
    }

    public static void whileStatement(){
        int counter = 0;
        int i = 10;
        while(i > 0){
            counter ++;
            i--;
        }
        System.out.println("While result: " + counter);
    }

    public static void doWhileStatement(){
        int i = 0;
        System.out.println("DoWhile Result: ");
        do{
            System.out.println("Here");
        }while(i > 0);

    }

    public static void forStatement(){
        int[] element = { 2312 ,123_23,123,656,4};

        for( int i = 0; i < element.length ; i++ ) {
            System.out.println("Hello World " + element[i]);
        }

        int x = 0;
        for(long y = 0, z = 4; x < 5 && y < 10; x++, y++) {
            System.out.print(y + " ");
        }
        System.out.print(x);

    }

    public static void forEachStatement(){
        final String[] names = new String[3];
        names[0] = "Lisa";
        names[1] = "Kevin";
        names[2] = "Roger";

        for(String name : names) {
            System.out.print(name + ", ");
        }

    }

    public static void breakStatement(){
        int[][] mycomplexarray = {{5,2,1,3},{10,11,8,9},{5,7,12,7}};
        int counter = 0;
        outer_loop: for(int[] mysimplearray : mycomplexarray) {
            for(int i=0; i<mysimplearray.length; i++) {
                if(counter == 7)
                    break outer_loop;
                if(mysimplearray[i] == 11)
                    break;
                counter++;
                System.out.print(mysimplearray[i]+"\t");
            }
            System.out.println();
        }

    }

    public static void continueStatement(){
        int[] vector = { 4,6,8,2,12};
        int  sum = 0;
        for (int i : vector){
            if(i == 8){
                continue;
            }
            sum += i;
        }
        System.out.println("The sum is: " + sum);
    }
}
