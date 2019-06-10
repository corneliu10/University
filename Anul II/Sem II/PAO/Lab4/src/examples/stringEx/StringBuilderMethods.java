package examples.stringEx;

public class StringBuilderMethods {
    public static void main(String args[]){
        // append method
        StringBuilder sb=new StringBuilder("Hello ");
        sb.append("Java");//now original string is changed
        System.out.println(sb);//prints Hello Java

        // insert method
        StringBuilder sb2=new StringBuilder("Hello ");
        sb2.insert(1,"Java");//now original string is changed
        System.out.println(sb2);//prints HJavaello

        // replace method
        StringBuilder sb3=new StringBuilder("Hello");
        sb3.replace(1,3,"Java");
        System.out.println(sb3);//prints HJavalo

        //delete method
        StringBuilder ssb=new StringBuilder("Hello");
        ssb.delete(1,3);
        System.out.println(ssb);//prints Hlo

        // reverse method
        StringBuilder ssb3=new StringBuilder("Hello");
        ssb3.reverse();
        System.out.println(ssb3);//prints olleH
    }

}
