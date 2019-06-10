package lab1.tasks.task5;

import java.util.Scanner;

public class Main {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        processSumOfBigNumbers(sc);
    }

    public static void processSumOfBigNumbers(Scanner sc)
    {
        String firstNumber = sc.next(); // first Number
        String secondNumber = sc.next(); // second Number

        String result = sumOf(new StringBuilder(firstNumber), new StringBuilder(secondNumber));
        System.out.println(result);
    }

    public static void processOperation(Scanner sc)
    {
        char operation = sc.next().charAt(0);

        int firstNumber = sc.nextInt();
        int secondNumber = sc.nextInt();

        switch (operation) {
            case '+':
                System.out.println("Result: " + (firstNumber + secondNumber));
                break;
            case '*':
                System.out.println("Result: " + (firstNumber * secondNumber));
                break;
            case '/':
                System.out.println("Result: " + (firstNumber / secondNumber));
                break;
            case '-':
                System.out.println("Result: " + (firstNumber - secondNumber));
                break;
            default:
                break;
        }
    }

    public static String sumOf(StringBuilder s1, StringBuilder s2)
    {
        if (s1.length() > s2.length())
        {
            StringBuilder temp = s1;
            s1 = s2;
            s2 = temp;
        }

        s1 = s1.reverse();
        s2 = s2.reverse();

        StringBuilder result = new StringBuilder("");

        int rest = 0;
        for (int i = 0; i < s1.length(); ++i)
        {
            int sum = ((int)(s1.charAt(i) - '0') + (int)(s2.charAt(i) - '0') + rest);
            result.append((char)(sum % 10 + '0'));

            rest = sum / 10;
        }

        for (int i = s1.length(); i < s2.length(); ++i)
        {
            int sum = (int)(s2.charAt(i) - '0') + rest;
            result.append((char)(sum % 10 + '0'));

            rest = sum / 10;
        }

        if (rest > 0)
            result.append((char)(rest - '0'));

        result = result.reverse();
        return result.toString();
    }
}
