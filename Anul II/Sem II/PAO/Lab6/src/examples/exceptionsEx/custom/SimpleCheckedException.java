package examples.exceptionsEx.custom;

public class SimpleCheckedException extends Exception{

    public SimpleCheckedException() {
        // TODO Auto-generated constructor stub
    }

    public SimpleCheckedException(String message) {
        super(message);
        // TODO Auto-generated constructor stub
    }

    public SimpleCheckedException(Throwable cause) {
        super(cause);
        // TODO Auto-generated constructor stub
    }

    public SimpleCheckedException(String message, Throwable cause) {
        super(message, cause);
        // TODO Auto-generated constructor stub
    }

    public SimpleCheckedException(String message, Throwable cause, boolean enableSuppression,
                                 boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
        // TODO Auto-generated constructor stub
    }
}
