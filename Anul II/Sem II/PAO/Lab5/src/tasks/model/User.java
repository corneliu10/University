package tasks.model;

import tasks.auth.Authenticable;

import java.util.Date;

public class User implements Authenticable {
    private String firstName;
    private String lastName;
    private Date dateOfBirth;

    private String userName;
    private String hashPassword;
    private String token = null;

    public User(String firstName, String lastName, Date dateOfBirth, String userName, String hashPassword) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.dateOfBirth = dateOfBirth;
        this.userName = userName;
        this.hashPassword = hashPassword;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(Date dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    @Override
    public String getToken() {
        return token == null ? Authenticable.DEFAULT_TOKEN : token;
    }

    @Override
    public String getUserName() {
        return userName;
    }

    @Override
    public String getHashPassword() {
        return hashPassword;
    }
}
