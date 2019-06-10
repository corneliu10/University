package tasks;

import tasks.model.AuthType;
import tasks.model.User;

public class Main {
    public static void main(String[] args) {
        User user = new User(AuthType.DB);
        performAuthentication(user);

        user.setAuthType(AuthType.LDAP);
        performAuthentication(user);

        user.setAuthType(AuthType.DEFAULT);
        performAuthentication(user);
    }

    private static void performAuthentication(User user) {
        try {
            user.performAuthentication();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
