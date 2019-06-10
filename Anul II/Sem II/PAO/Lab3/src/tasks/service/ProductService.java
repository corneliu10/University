package tasks.service;

import tasks.model.Category;
import tasks.model.Price;
import tasks.model.Product;

public class ProductService {
    private static ProductService instance = new ProductService();
    private static Product[] listOfProduct = new Product[4];

    private ProductService() {
        listOfProduct[0] = new Product(new Category(), new Price(), "Product One", "one");
        listOfProduct[0] = new Product(new Category(), new Price(), "Product One", "one");
        listOfProduct[0] = new Product(new Category(), new Price(), "Product One", "one");
        listOfProduct[0] = new Product(new Category(), new Price(), "Product One", "one");
    }

    public static ProductService getIstance() {
        return instance;
    }

    public Product getOne(String name) {
        for (Product product : listOfProduct) {
            if (product.getName().equals(name))
                return product;
        }

        return null;
    }

    public Product getOne(Price price) {
        for (Product product : listOfProduct) {
            if (product.getPrice().equals(price))
                return product;
        }

        return null;
    }
}
