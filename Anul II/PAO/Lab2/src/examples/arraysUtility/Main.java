package examples.arraysUtility;

import java.util.Arrays;

/**
 * Created by bogdan pahontu
 */
public class Main {
    public static void main(String args[]){
        Integer[] arr = {4, 6, 7};

        Integer[][] a = {{1, 2, 3}, {4, 5, 6}};

        // Transforming an array into a string
        System.out.println("arrays: " + Arrays.toString(arr));
        for (int i = 0; i < a.length; i++) {
            System.out.println("arrays, row " + i + " : " + Arrays.toString(a[i]));
        }

        Integer myIntegerTable[] = {null, null, null};
        Arrays.fill(myIntegerTable, 12); // umplere a tuturor elementelor cu acelasi elemnt 12
        System.out.println("myIntegerTable: " + Arrays.toString(myIntegerTable));


        String[] arrayOfStrings = {"10","1","2","21","32","3"};
        Arrays.sort(arr);
        Arrays.sort(arrayOfStrings);
        System.out.println("arr: " + Arrays.toString(arr));
        System.out.println("arr: " + Arrays.toString(arrayOfStrings));


        String[] arraySearch = {"ala", "pestisor", "bala", "portocala"};

        int searchResult = Arrays.binarySearch(arraySearch, "bala");

        Arrays.sort(arraySearch);
        int searchResult2 = Arrays.binarySearch(arraySearch, "bala");

        System.out.println("searching word bala, result: " + searchResult);
        System.out.println("searching word bala, result after sorting: " + searchResult2);
    }
}
