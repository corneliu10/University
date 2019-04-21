package examples.generics;

public class GenericCls {
    public static void main (String[] args)
    {
        // instance of Integer type
        TestGeneric <Integer> iObj = new TestGeneric<Integer>(15);
        genericDisplay(iObj.getObject());

        // instance of String type
        TestGeneric <String> sObj =
                new TestGeneric<String>("This a test");
        genericDisplay(sObj.getObject());
    }


    // A Generic method example
    static <T> void genericDisplay (T element)
    {
        System.out.println(element.getClass().getName() +
                " = " + element);
    }
}

// A generic class example
class TestGeneric<T> {
    T obj;

    TestGeneric(T obj) {
        this.obj = obj;
    }

    public T getObject() {
        return this.obj;
    }
}
