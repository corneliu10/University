package tasks.model;

import java.util.Date;

public class Price implements Cloneable {
    private Double price;
    private Date startForm;
    private Date endForm;

    public Price() {

    }

    public Price(Double price, Date startForm, Date endForm) {
        this.price = price;
        this.startForm = startForm;
        this.endForm = endForm;
    }

    public Double getPrice() {
        return price;
    }

    public Date getEndForm() {
        return endForm;
    }

    public Date getStartForm() {
        return startForm;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public void setStartForm(Date startForm) {
        this.startForm = startForm;
    }

    public void setEndForm(Date endForm) {
        this.endForm = endForm;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public boolean equals(Object obj) {
        return startForm.equals(((Price) obj).startForm)
               && endForm.equals(((Price) obj).endForm)
               && (price != ((Price) obj).price);
    }
}
