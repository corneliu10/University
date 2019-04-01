package tasks.customer;

import tasks.model.User;

import java.util.Date;

public class Customer extends User {
    CustomerDetails customerDetails;

    public Customer(String firstName, String lastName, Date dateOfBirth, String userName, String hashPassword) {
        super(firstName, lastName, dateOfBirth, userName, hashPassword);
    }

    public CustomerDetails getCustomerDetails() {
        return customerDetails;
    }

    public void setCustomerDetails(CustomerDetails customerDetails) {
        this.customerDetails = customerDetails;
    }
}
