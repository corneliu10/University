package lab1.tasks.task4;

public class Main {
    public static void main(String args[])
    {
        int[][] matrix = {{5,2,1},{3,4,2},{5,2,8}};
        for (int[] array : matrix) {
            for (int i = 0; i < array.length; ++i)
                System.out.print(array[i]);
            System.out.println();
        }
    }
}
