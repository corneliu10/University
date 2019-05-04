package examples.components.formExample;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SecondFormExample {
    public static void main(String[] args) {
        JFrame f=new JFrame();//creating instance of JFrame
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel l1,l2,l3,l4,l5,l6,l7,l8;
        l1=new JLabel("Form Swing");
        l1.setBounds(150,50, 100,30);
        f.add(l1);

        l2=new JLabel("Name");
        l2.setBounds(50,100, 100,30);
        f.add(l2);

        JTextField t1,t2,t3;
        t1=new JTextField();
        t1.setBounds(100,100, 100,30);
        f.add(t1);

        l3=new JLabel("Phone");
        l3.setBounds(50,150, 100,30);
        f.add(l3);

        t2=new JTextField();
        t2.setBounds(100,150, 100,30);
        f.add(t2);

        l4=new JLabel("Email");
        l4.setBounds(50,200, 100,30);
        f.add(l4);

        t3=new JTextField();
        t3.setBounds(100,200, 200,30);
        f.add(t3);

        l5=new JLabel("Sex");
        l5.setBounds(50,250, 100,30);
        f.add(l5);

        ButtonGroup buttonGroup = new ButtonGroup();
        JRadioButton r1,r2;
        r1 = new JRadioButton("Male");
        r2 = new JRadioButton("Female");
        buttonGroup.add(r1);
        buttonGroup.add(r2);

        r1.setBounds(100,250, 100,30);
        r2.setBounds(200,250, 100,30);
        f.add(r1);
        f.add(r2);

        l6=new JLabel("Occupation");
        l6.setBounds(50,300, 100,30);
        f.add(l6);

        JComboBox comboBox = new JComboBox();
        comboBox.addItem("Select");
        comboBox.addItem("Business");
        comboBox.addItem("Engineer");
        comboBox.addItem("Doctor");
        comboBox.addItem("Student");
        comboBox.addItem("Others");
        comboBox.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
            }
        });
        comboBox.setBounds(150, 300, 100, 20);
        f.add(comboBox);

        l7=new JLabel("Interested of: ");
        l7.setBounds(50,350, 100,30);
        f.add(l7);

        JCheckBox checkBox1 = new JCheckBox("C++");
        checkBox1.setBounds(50,370, 150,50);
        JCheckBox checkBox2 = new JCheckBox("Java");
        checkBox2.setBounds(50,400, 150,50);
        JCheckBox checkBox3 = new JCheckBox("Php");
        checkBox3.setBounds(50,430, 150,50);
        f.add(checkBox1);
        f.add(checkBox2);
        f.add(checkBox3);

        JButton b=new JButton("Save");//creating instance of JButton
        b.setBounds(50,500,100, 40);//x axis, y axis, width, height

        f.add(b);//adding button in JFrame

        JButton b2=new JButton("Cancel");//creating instance of JButton
        b2.setBounds(300,500,100, 40);//x axis, y axis, width, height

        f.add(b2);//adding button in JFrame

        f.setSize(500,600);//400 width and 500 height
        f.setLayout(null);//using no layout managers
        f.setVisible(true);//making the frame visible
    }
}
