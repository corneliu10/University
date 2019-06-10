package examples.jdbc;

import java.sql.*;

public class DbSelect {
    public static void main(String args[]) throws SQLException {
        Connection conn = ConnectionUtils.getDBConnection();
        selectById(conn, 3);
        selectWithException(conn);
    }

    public static void selectById(Connection connection, int uid) {
        String sql = "SELECT * FROM users WHERE id = ?";
        try {
            PreparedStatement pstmt = connection.prepareStatement(sql);
            pstmt.setDouble(1, uid);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String username = rs.getString("username");
                System.out.println("id: " + id + " name: " + name + " username:" + username);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void selectWithException(Connection conn) {
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("select not_a_column from users");
            while (rs.next())
                System.out.println(rs.getString(1));
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            System.out.println(e.getSQLState());
            System.out.println(e.getErrorCode());
        }
    }
}
