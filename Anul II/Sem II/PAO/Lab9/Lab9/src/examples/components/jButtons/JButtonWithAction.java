package examples.components.jButtons;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JButtonWithAction {
    public static void main(String[] args) {
        // The frame
        JFrame f = new JFrame("Button Example with Action Listener");

        // The textfield
        JTextField tf = new JTextField();
        tf.setBounds(50, 50, 300, 20);

        // The button
        JButton b = new JButton("Click Me");
        b.setBounds(50, 100, 95, 30);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                tf.setText("This is the text displayed after the button was pressed.");
            }
        });
        f.add(b);
        f.add(tf);
        f.setSize(400, 400);
        f.setLayout(null);
        f.setVisible(true);
    }
}
