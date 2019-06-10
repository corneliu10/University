package examples.jdbc;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class DbExecuteUpdate {
    public static void main(String args[]){
        Connection conn = ConnectionUtils.getDBConnection();
        execUpdate(conn);
        ConnectionUtils.closeDBConnection(conn);
    }

    public static void execUpdate(Connection conn){
        try {
            Statement stmt = conn.createStatement();
            int result = stmt.executeUpdate("insert into users(username) values('Ben')");
            System.out.println(result); // 1
            result = stmt.executeUpdate("update users set name = 'Ben Edited' where username = 'Ben'");
            System.out.println(result); // 0
            result = stmt.executeUpdate("delete from users where id = 10");
            System.out.println(result); // 1
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
