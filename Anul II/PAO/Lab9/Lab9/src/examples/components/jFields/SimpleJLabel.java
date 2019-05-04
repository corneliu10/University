package examples.components.jFields;

import javax.swing.*;

public class SimpleJLabel {
    public static void main(String args[]) {
        JFrame f = new JFrame("Label Example");

        JLabel l1;
        l1 = new JLabel("This is a label created for demo purpose");
        l1.setBounds(50, 50, 300, 30);

        f.add(l1);
        f.setSize(600, 600);
        f.setLayout(null);
        f.setVisible(true);
    }
}
