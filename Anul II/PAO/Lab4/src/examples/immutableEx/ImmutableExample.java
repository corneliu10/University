package examples.immutableEx;

public final class ImmutableExample {
    final String name;
    final int regNo;

    public ImmutableExample(String name, int regNo) {
        this.name = name;
        this.regNo = regNo;
    }

    public String getName()
    {
        return name;
    }
    public int getRegNo()
    {
        return regNo;
    }
}
