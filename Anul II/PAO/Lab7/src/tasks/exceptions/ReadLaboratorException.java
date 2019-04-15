package tasks.exceptions;

import java.io.IOException;

public class ReadLaboratorException extends IOException {
    private String Name = new String("Read Exception");

    public ReadLaboratorException() {
        super();
    }

    public ReadLaboratorException(String message) {
        super(message);
    }

    public String getName() {
        return Name;
    }
}
