package tasks.services;

import tasks.auth.Authenticable;

public class UserService {
    boolean checkDefToken(Authenticable auth) {
        return auth.DEFAULT_TOKEN.equals("TEST");
    }
}
