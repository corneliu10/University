package examples.constructors;

/**
 * Created by bogdan pahontu
 */
public class Animal {
    private String name;
    private String type;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void printAnimal(){
        System.out.println("Name: " + this.name + "; Type: " + this.type);
    }
}
