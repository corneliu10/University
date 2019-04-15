package tasks.exceptions;

import java.io.IOException;

public class WriteLaboratorException extends IOException {
    private String Name = new String("Write Exception");

    public WriteLaboratorException() {
        super();
    }

    public WriteLaboratorException(String message) {
        super(message);
    }

    public String getName() {
        return Name;
    }
}
