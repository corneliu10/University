package tasks.model;

import tasks.exception.UserAuthException;

public class User implements AuthenticableDB, AuthenticableLDAP {
    private String name;
    private String hashPassword;
    private AuthType authType;

    public User(AuthType authType) {
        this.authType = authType;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getHashPassword() {
        return hashPassword;
    }

    public void setHashPassword(String hashPassword) {
        this.hashPassword = hashPassword;
    }

    public AuthType getAuthType() {
        return authType;
    }

    public void setAuthType(AuthType authType) {
        this.authType = authType;
    }

    @Override
    public void performAuthentication() throws Exception {
        switch (authType) {
            case DB:
                AuthenticableDB.super.performAuthentication();
                break;
            case LDAP:
                AuthenticableLDAP.super.performAuthentication();
                break;
            default:
                throw new UserAuthException("Default Error");
        }
    }
}
