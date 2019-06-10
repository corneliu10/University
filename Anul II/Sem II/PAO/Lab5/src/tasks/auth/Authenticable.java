package tasks.auth;

public interface Authenticable {
    public static final String DEFAULT_TOKEN = "TEST";

    String getToken();
    default String getUserName() {
        return "someusername";
    }
    default String getHashPassword() {
        return "somepass";
    }
}
