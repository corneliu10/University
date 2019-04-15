package tasks.task1;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Invoice implements Serializable {
    private String code;
    private Date date;
    private List<Item> listOfItems;

    public Invoice(String code, Date date) {
        this.code = code;
        this.date = date;
        this.listOfItems = new ArrayList<>();
    }

    public Invoice(String code, Date date, List<Item> listOfItems) {
        this.code = code;
        this.date = date;
        this.listOfItems = listOfItems;
    }

    @Override
    public String toString() {
        return code + " " + date.toString() + " " + listOfItems.size();
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public List<Item> getListOfItems() {
        return listOfItems;
    }

    public void setListOfItems(List<Item> listOfItems) {
        this.listOfItems = listOfItems;
    }
}
