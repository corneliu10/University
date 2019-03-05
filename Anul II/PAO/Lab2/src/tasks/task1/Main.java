package tasks.task1;

public class Main {
    public static void main(String args[])
    {
        Integer table1[][] = {{1, 2, 3}, {3, 4, 5, 5}};
        printTable(table1);
    }

    private static void printTable(Integer[][] table)
    {
        for (int i = 0; i < table.length; i++)
            for (int j = 0; j < table[i].length; j++)
                System.out.println(table[i][j]);
    }
}
