package examples.intellijGUIPlugin;

import javax.swing.*;

public class Main {
    public static void main(String[] args){
        JFrame frame = new JFrame("Gui Demo");
        frame.setContentPane(new DemoGUI().getView());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
