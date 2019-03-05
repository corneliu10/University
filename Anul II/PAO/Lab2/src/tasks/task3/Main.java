package tasks.task3;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String args[])
    {
        Integer[] array = {1, 2, 3, 4};
        findAndCopy(array, 4);
    }

    public static void findAndCopy(Integer[] array, Integer item)
    {
        int index = -1;
        for (int i = 0; i < array.length; ++i)
            if (array[i] == item) {
                index = i;
                break;
            }

        if (index > -1) {
            Integer[] subArray = Arrays.copyOfRange(array, index, array.length);
            for (int i = 0; i < subArray.length; ++i)
                System.out.println(subArray[i]);
        } else {
            System.out.println("No item found in the array!");
        }

    }
}
