package examples.exceptionsEx;

public class TryWIthReturnExample {
    public static void main(String[] args){
        performFinally();
    }

    public static int performFinally(){
        int result = 1;
        try{
            result = 2;
            throw new NullPointerException("This is my null pointer exception");

        }catch(Exception ex){
            ex.printStackTrace();
            return 0;
        }finally {
            result = 4;
            System.out.println("Finally block");
            return result;
        }
    }
}
