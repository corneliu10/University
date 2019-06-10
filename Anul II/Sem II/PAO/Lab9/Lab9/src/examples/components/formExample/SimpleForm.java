package examples.components.formExample;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class SimpleForm {
    public static void main(String[] args) {
        // The frame
        JFrame loginFrame = new JFrame("Simple form example");


        JLabel usernameLabel, passwordLabel;
        usernameLabel = new JLabel("Username");
        usernameLabel.setBounds(50, 50, 300, 30);

        // The textfield
        JTextField usernameField = new JTextField();
        usernameField.setBounds(50, 80, 300, 20);


        passwordLabel = new JLabel("Password");
        passwordLabel.setBounds(50, 100, 300, 30);

        // The textfield
        JTextField passwordField = new JPasswordField();
        passwordField.setBounds(50, 130, 300, 20);


        // The button
        JButton submit = new JButton("Submit");
        submit.setBounds(50, 180, 95, 30);



        // The console field
        JTextArea consoleField = new JTextArea("Console:");
        consoleField.setBounds(0, 300, 400, 150);
        consoleField.setAutoscrolls(true);

        submit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                consoleField.append("\nAttempt to login using username: " + usernameField.getText());
            }
        });


        loginFrame.add(usernameField);
        loginFrame.add(usernameLabel);
        loginFrame.add(passwordField);
        loginFrame.add(passwordLabel);
        loginFrame.add(consoleField);
        loginFrame.add(submit);
        loginFrame.setSize(400, 400);
        loginFrame.setLayout(null);
        loginFrame.setVisible(true);
    }
}
