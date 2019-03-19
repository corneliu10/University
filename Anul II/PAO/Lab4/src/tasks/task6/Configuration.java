package tasks.task6;

public final class Configuration {
    private final String dbConnectionString;
    private final String externalResourcesPath;
    private final String environment;

    public Configuration(String dbConnectionString, String externalResourcesPath, String environment) {
        this.dbConnectionString = dbConnectionString;
        this.externalResourcesPath = externalResourcesPath;
        this.environment = environment;
    }

    public String getDbConnectionString() {
        return dbConnectionString;
    }

    public String getExternalResourcesPath() {
        return externalResourcesPath;
    }

    public String getEnvironment() {
        return environment;
    }
}
