package examples.jdbc;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.SQLException;

public class DatabaseMeta {
    public static void main(String args[]) throws SQLException{
        Connection conn = ConnectionUtils.getDBConnection();
        printDatabaseDetails(conn);
        ConnectionUtils.closeDBConnection(conn);
    }

    public static void printDatabaseDetails(Connection connection) throws SQLException {
        DatabaseMetaData meta = connection.getMetaData();
        System.out.println("The driver name is " + meta.getDriverName());
    }
}
