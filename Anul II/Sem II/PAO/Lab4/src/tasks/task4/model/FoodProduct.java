package tasks.task4.model;

public class FoodProduct extends Product {

    @Override
    public String getName() {
        return super.getName() + " : Food";
    }

    @Override
    public int roundPrice() {
        return 0;//price.getPrice();
    }

    @Override
    public void print() {
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(this.getName());
        stringBuilder.append(" ");
        stringBuilder.append(this.getSmallDescription());
        stringBuilder.append(" ");
        stringBuilder.append(this.price.toString());

        return stringBuilder.toString();
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
