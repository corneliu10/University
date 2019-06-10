package tasks.services;

import tasks.auth.Authenticable;
import tasks.customer.Customer;
import tasks.model.User;

import java.util.Date;

public class Main {
    public static void main(String[] args) {
        Authenticable auth = new Customer("Corneliu", "Dumitru", new Date(), "waka", "maca");
        UserService userService = new UserService();
        System.out.println(userService.checkDefToken(auth));
    }
}
