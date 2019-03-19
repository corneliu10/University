package examples.stringEx;

public class StringMethods {
    public static void main(String[] args){
        // length() function
        String palindrome = "Dot saw I was Tod";
        int len = palindrome.length();
        System.out.println( "String Length is : " + len );


        // concat() function
        String ss1 = "This is ";
        String ss2 = "an example";
        ss1.concat(ss2);
        System.out.println(ss1);
        String s3 = ss1.concat(ss2);
        System.out.println(s3);

        // format() function
        String fs;
        Float floatVar = 1.2f;
        Integer intVar = 5;
        String stringVar = "test";
        fs = String.format("The value of the float variable is " +
                "%f, while the value of the integer " +
                "variable is %d, and the string " +
                "is %s", floatVar, intVar, stringVar);
        System.out.println(fs);

        //split() function
        String str = "hello@world";
        String[] arrOfStr = str.split("@", 2);
        for (String a : arrOfStr)
            System.out.println(a);

        //indexOf() function
        String str1 = new String("This is a Tutorial");
        System.out.println("Index of o in str: "+str1.indexOf('o'));

        //lastIndexOf() function
        String s1="This is index of example";
        int index1=s1.lastIndexOf('s');
        System.out.println(index1);//6

        //toLowerCase() function
        String str2 = new String("ABC IS NOT EQUAL TO XYZ");
        System.out.println(str2.toLowerCase());

        //toUpperCase() function
        String s2="hello string";
        String s2upper=s2.toUpperCase();
        System.out.println(s2upper);

        //substring() function
        String substr = "howtodoinjava";
        System.out.println(substr.substring(3));  //todoinjava
        System.out.println("hello world".substring(6)); //world

        //startsWith() function
        //given string
        String start = "This is just a sample string";
        System.out.println(start.startsWith("This"));  //true
        System.out.println(start.startsWith("Hi"));  //false

        //endsWith() function
        String end = "Java String endsWith example";
        System.out.println("EndsWith character 'e': " + end.endsWith("e")); //true
        System.out.println("EndsWith character 'ple': " + end.endsWith("ple")); //true
        System.out.println("EndsWith character 'Java': " + end.endsWith("Java")); //false
    }
}
