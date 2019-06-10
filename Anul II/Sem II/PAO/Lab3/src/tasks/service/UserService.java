package tasks.service;

import tasks.model.User;

public class UserService {
    private static UserService instance = new UserService();
    private static User[] listOfUsers = new User[4];

    private UserService() {
        listOfUsers[0] = new User(1, "Ioana", "password");
        listOfUsers[1] = new User(2, "Adelin", "password");
        listOfUsers[2] = new User(3, "Marcu", "password");
        listOfUsers[3] = new User(4, "Doru", "password");
    }

    public static UserService getInstance() {
        return instance;
    }

    public User getOne(Integer id) {
        for (User user : listOfUsers) {
            if (user.getId() == id)
                return user;
        }

        return null;
    }

    public User getOne(String username) {
        for (User user : listOfUsers) {
            if (user.getUsername().equals(username))
                return user;
        }

        return null;
    }
}
