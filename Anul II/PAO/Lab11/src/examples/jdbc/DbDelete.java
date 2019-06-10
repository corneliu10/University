package examples.jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DbDelete {
    public static void main(String args[]) throws SQLException {
        Connection conn = ConnectionUtils.getDBConnection();
        deleteById(conn,4);
        ConnectionUtils.closeDBConnection(conn);
    }

    public static void deleteById(Connection connection, int id) {
        String sql = "DELETE FROM users WHERE id = ?";
        try {
            PreparedStatement pstmt = connection.prepareStatement(sql);
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
