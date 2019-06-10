package examples.jdbc;

import java.sql.*;

public class SimpleExample {
    public static void main(String args[]) {
        try {
            // Incarcam clasa
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Crearea unei conexiuni
            Connection connection = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/store?serverTimezone=UTC",
                    "root",
                    "root");

            // Creare unui statement
            Statement statement = connection.createStatement();

            //Executie query
            ResultSet rs = statement.executeQuery("select * from users");

            while (rs.next()) {
                System.out.println("User id: " + rs.getInt(1));
                System.out.println("Username: " + rs.getString(2));
                System.out.println("Birth Date: " + rs.getDate(4));
            }

            // Afisare Metadata
            ResultSetMetaData resultSetMetaData = rs.getMetaData();

            for (int i = 1; i <= resultSetMetaData.getColumnCount(); i++) {
                System.out.println("column name: " + resultSetMetaData.getColumnName(i)
                        + ", column type: " + resultSetMetaData.getColumnType(i));
            }

        } catch (ClassNotFoundException ex) {
            ex.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
