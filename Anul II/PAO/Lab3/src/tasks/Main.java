package tasks;

import tasks.model.*;

public class Main {
    public static void main(String[] args) {
        Product product = new Product();
        product.setName("Product one");

        FoodProduct foodProduct = new FoodProduct();
        foodProduct.setName("Product two");

        System.out.println("Product: " + product.getName());
        System.out.println("Product: " + foodProduct.getName());

        Product foodProduct2 = new FoodProduct();
        foodProduct2.setName("foodProduct");
        System.out.println("FP: " + foodProduct2.getName());
    }
}
