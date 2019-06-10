package examples.components.jFields;

import javax.swing.*;

public class SimpleJField {
    public static void main(String args[]) {
        JFrame f = new JFrame("TextField Example");
        JTextField t1, t2;
        t1 = new JTextField("Name.");
        t1.setBounds(50, 100, 200, 30);

        f.add(t1);
        f.setSize(500, 500);
        f.setLayout(null);
        f.setVisible(true);
    }
}
