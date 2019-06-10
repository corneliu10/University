package tasks.task4.model;

public class Category implements Cloneable {
    private String name;
    private String description;
    Category parent;

    public Category getParent() {
        return parent;
    }

    public String getDescription() {
        return description;
    }

    public String getName() {
        return name;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setParent(Category parent) {
        this.parent = parent;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}
