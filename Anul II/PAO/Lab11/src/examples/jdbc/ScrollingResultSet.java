package examples.jdbc;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ScrollingResultSet {
    public static void main(String args[]) throws SQLException{
        Connection conn = ConnectionUtils.getDBConnection();
        scrollingResultSetExample(conn);
        ConnectionUtils.closeDBConnection(conn);
    }

    public static void scrollingResultSetExample(Connection connection) throws SQLException {
        Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,
                ResultSet.CONCUR_READ_ONLY);
        ResultSet rs = stmt.executeQuery("select id from users order by id");
        rs.afterLast();
        System.out.println(rs.previous()); // true
        System.out.println(rs.getInt(1)); // 2
        System.out.println(rs.previous()); // true
        System.out.println(rs.getInt(1)); // 1
        System.out.println(rs.last()); // true
        System.out.println(rs.getInt(1)); // 2
        System.out.println(rs.first()); // true
        System.out.println(rs.getInt(1)); // 1
        rs.beforeFirst();
        rs.next();
        System.out.println(rs.getInt(1));
    }
}
