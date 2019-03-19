package tasks.task4.model;

public class InvoiceItem {
    private Product product;
    private double TVA = 24.0;

    public InvoiceItem(Product product, double TVA) {
        this.product = product;
        this.TVA = TVA;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    public double getTVA() {
        return TVA;
    }

    public void setTVA(double TVA) {
        this.TVA = TVA;
    }
}
