package tasks.model;

public interface AuthenticableDB extends Authenticable {
    private void performDBAuth() {
        System.out.println("performDBAuth");
    }

    @Override
    default void performAuthentication() throws Exception {
        performDBAuth();
    }
}
