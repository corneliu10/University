package tasks.task4.model;

public abstract class Product implements Cloneable {
    private Category category;
    protected Price price;
    protected String name;
    private String smallDescription;

    public Product() {
    }

    public Product(Category category, Price price, String name, String smallDescription) {
        this.category = category;
        this.price = price;
        this.name = name;
        this.smallDescription = smallDescription;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

    public Price getPrice() {
        return price;
    }

    public void setPrice(Price price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSmallDescription() {
        return smallDescription;
    }

    public void setSmallDescription(String smallDescription) {
        this.smallDescription = smallDescription;
    }

    public abstract int roundPrice();

    public abstract void print();

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
