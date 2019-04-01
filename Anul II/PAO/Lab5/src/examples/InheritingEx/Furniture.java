package examples.InheritingEx;

public class Furniture implements HasDepth,HasHeight,HasWidth {
    int depth;
    int height;
    int width;

    public Furniture(int depth, int height, int width) {
        this.depth = depth;
        this.height = height;
        this.width = width;
    }

    public int getDepth(){
        return this.depth;
    }

    public int getHeight(){
        return this.height;
    }

    public int getWidth(){
        return this.width;
    }

    public String getPropertyName(){
        return "This is a property";
    }
}
