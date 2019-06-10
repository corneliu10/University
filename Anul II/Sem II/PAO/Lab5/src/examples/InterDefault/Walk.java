package examples.InterDefault;

public interface Walk {
    public default int getSpeed(){
        return 5;
    }
}



