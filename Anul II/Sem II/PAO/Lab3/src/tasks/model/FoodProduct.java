package tasks.model;

public class FoodProduct extends Product {

    @Override
    public String getName() {
        return super.getName() + " : Food";
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
