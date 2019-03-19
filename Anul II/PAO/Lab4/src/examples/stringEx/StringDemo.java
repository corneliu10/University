package examples.stringEx;

public class StringDemo {

    public static void main(String[] args){
        // declaring a String
        String string = "my first string";
        String otherString = new String("other string");
        String thirdString = string + ", " + otherString;

        System.out.println("thirdString: " + thirdString);

        // search for a string in a string
        int i = thirdString.indexOf(", ");
        System.out.println("find \", \" at position: " + i);

        // search for a char in a string, instead of double quote we have simple quotes
        System.out.println("find ','  at position: " + thirdString.indexOf(','));

        // substring start from a positiion till the end
        String forthString = thirdString.substring(i + 2);
        System.out.println("forthString: " + forthString);

        // begin, end -  stop at a defined end
        forthString = thirdString.substring(i + 2, i + 2 + 5);
        System.out.println("forthString: " + forthString);

        // begin, end -  stop at a defined end after real end,
        // will result in an exception Exception in thread "main" java.lang.StringIndexOutOfBoundsException: String index out of range
//        forthString = thirdString.substring(i + 2, i + 2 + 5 + 25);
        System.out.println("forthString: " + forthString);

        // String create from StringBuilder
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("un string urmat de un integer: ").append(22).append(", apoi de un caracter").append(';');
        String fifthString = new String(stringBuilder);
        System.out.println("fifthString: " + fifthString);
        // or
        System.out.println("stringBuilder: " + stringBuilder.toString());

    }
}
