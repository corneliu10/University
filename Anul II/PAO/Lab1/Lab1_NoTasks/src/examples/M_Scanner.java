package examples;

import java.util.Scanner;

/**
 * Created by bogdan pahontu
 */
public class M_Scanner {
    public static void main(String args[]){
        // Declare the object and initialize with
        // predefined standard input object
        Scanner sc = new Scanner(System.in);

        // String input
        System.out.println("Insert a name");
        String name = sc.nextLine();

        // Character input
        System.out.println("Insert gender M/F");
        char gender = sc.next().charAt(0);

        // Numerical data input
        // byte, short and float can be read
        // using similar-named functions.
        System.out.println("Insert the age");
        int age = sc.nextInt();

        System.out.println("Insert the mobile number");
        long mobileNo = sc.nextLong();

        // Print the values to check if input was correctly obtained.
        System.out.println("Name: "+name);
        System.out.println("Gender: "+gender);
        System.out.println("Age: "+age);
        System.out.println("Mobile Number: "+mobileNo);
    }
}
