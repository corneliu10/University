package tasks.task4.model;

import java.util.Date;

public class Invoice {
    private Date invoiceDate;
    private String invoiceName;

    private InvoiceItem[] invoices;

    public Invoice(Date invoiceDate, String invoiceName, InvoiceItem[] invoices) {
        this.invoiceDate = invoiceDate;
        this.invoiceName = invoiceName;
        this.invoices = invoices;
    }

    public Date getInvoiceDate() {
        return invoiceDate;
    }

    public void setInvoiceDate(Date invoiceDate) {
        this.invoiceDate = invoiceDate;
    }

    public String getInvoiceName() {
        return invoiceName;
    }

    public void setInvoiceName(String invoiceName) {
        this.invoiceName = invoiceName;
    }

    public InvoiceItem[] getInvoices() {
        return invoices;
    }

    public void setInvoices(InvoiceItem[] invoices) {
        this.invoices = invoices;
    }
}
