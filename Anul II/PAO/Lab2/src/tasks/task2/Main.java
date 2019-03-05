package tasks.task2;

public class Main {
    public static void main(String args[])
    {
        Integer[][] matrix = { {1, 2, 3}, {2, 1, 4}, {3, 4, 4}};
        System.out.println(isSymmetric((matrix)));
    }

    public static boolean isSymmetric(Integer[][] matrix)
    {
        for (int i = 0; i < matrix.length; ++i) {
            if (matrix.length != matrix[i].length) return false;
            for (int j = i; j < matrix[i].length; j++)
                if (!matrix[i][j].equals(matrix[i + (j-i)][i]))
                    return false;
        }

        return true;
    }
}
