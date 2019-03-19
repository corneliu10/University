package tasks.task4.model;

public class FurnitureProduct extends Product {
    @Override
    public int roundPrice() {
        return 0;
    }

    @Override
    public void print() {
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(this.getName());
        stringBuilder.append(":");
        stringBuilder.append(this.getSmallDescription());
        stringBuilder.append(":");
        stringBuilder.append(this.price.toString());

        return stringBuilder.toString();
    }
}
