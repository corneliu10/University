package examples.arrays;

/**
 * Created by bogdan pahontu
 */
public class Main {
    public static void main(String args[]){
        System.out.println("-------- Arrays--------");
        // Ex 1
        Integer[] arr1 = {22, 33, 44};

        // Ex 2
        String arr2[] = {"one", "two", "three"};

        // Ex 3
        String arrn3[] = new String[]{"first string", "second string"};
        String arrn4[] = new String[10]; // without initialization
        arrn4[0] = "test";
        arrn4[1] = "test1";

        // Looping by index
        for (int i = 0; i < arr1.length; i++) {
            System.out.println("arr1["+i+"]: " + arr1[i]);
        }

        // Looping using foreach
        for (String s : arr2) {
            System.out.println("arr: " + s);
        }

        System.out.println("-------- Bidimensional Arrays--------");
        // Bi-dimensional arrays
        int[][] biArr = new int[10][20];
        biArr[0][0] = 1;

        System.out.println("arr[0][0] = " + biArr[0][0]);

        System.out.println("------------ Example 2 -------------------");
        int[][] biArr2 = { { 1, 2 }, { 3, 4 } };

        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                System.out.println("arr[" + i + "][" + j + "] = "
                        + biArr2[i][j]);

    }
}
