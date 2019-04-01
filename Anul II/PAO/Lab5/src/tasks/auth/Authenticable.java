package tasks.auth;

public interface Authenticable {
    public static final String DEFAULT_TOKEN = "abc";

    String getToken();
    String getUserName();
    String getHashPassword();
}
