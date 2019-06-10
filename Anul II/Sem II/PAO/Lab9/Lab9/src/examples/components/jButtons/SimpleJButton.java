package examples.components.jButtons;

import javax.swing.*;

public class SimpleJButton extends JFrame {
    JFrame myFrame;

    SimpleJButton(){
        JButton clickBtn = new JButton("Submit");
        clickBtn.setBounds(130,100,100, 40);
        add(clickBtn);//adding button on frame
        setSize(400,500);
        setLayout(null);
        setVisible(true);
    }

    public static void main(String args[]){
        new SimpleJButton();
    }
}
