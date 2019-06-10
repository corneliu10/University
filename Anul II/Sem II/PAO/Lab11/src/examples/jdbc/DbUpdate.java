package examples.jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DbUpdate {
    public static void main(String args[]) throws SQLException {
        Connection conn = ConnectionUtils.getDBConnection();
        updateById(conn,2);
        ConnectionUtils.closeDBConnection(conn);
    }

    public static void updateById(Connection conn , int id){
        String sql = "UPDATE USERS SET NAME = 'CHANGED NAME' WHERE id = ?";
        try {
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
