package examples.theObject;

public class MyCustomObject extends Object{

    static int last_roll = 100;
    int roll_no;

    public MyCustomObject() {
        this.roll_no = last_roll;
        last_roll++;
    }

    @Override
    public String toString() {
        return "My Custom Object " + super.toString();
    }

    @Override
    public int hashCode() {
        return roll_no;
    }
}
