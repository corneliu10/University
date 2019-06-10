package examples.jdbc;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class DbInsert {
    public static void main(String args[]) throws SQLException {
        Connection conn = ConnectionUtils.getDBConnection();
        insertData(conn, createInserts());
        ConnectionUtils.closeDBConnection(conn);
    }

    public static List<String> createInserts() {
        List<String> inserts = new ArrayList<>();
        inserts.add("INSERT INTO users(username,name,date_of_birth) VALUES ('Bob', 'Bob Dev', '1991-10-10')");
        inserts.add("INSERT INTO users(username,name,date_of_birth,cnp) VALUES ('John', 'John Tester', '1991-10-09', '123213213')");

        return inserts;
    }

    public static void insertData(Connection connection, List<String> inserts) {
        try {
            Statement stmt = connection.createStatement();
            for (String insert : inserts) {
                stmt.execute(insert);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
