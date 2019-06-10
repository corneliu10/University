package examples.generics;

import java.util.ArrayList;
import java.util.List;

public class LowerBound {
    public static void addCat(List<? super Cat> catList) {
        catList.add(new RedCat());
        System.out.println("Cat Added");
    }

    public static void main(String[] args) {
        List<Animal> animalList= new ArrayList<>();
        List<Cat> catList= new ArrayList<Cat>();
        List<RedCat> redCatList= new ArrayList<RedCat>();
        List<Dog> dogList= new ArrayList<Dog>();

        //add list of super class Animal of Cat class
        addCat(animalList);

        //add list of Cat class
        addCat(catList);

        //compile time error
        //can not add list of subclass RedCat of Cat class
        //addCat(redCatList);
    }
}

class Animal {}

class Cat extends Animal {}

class RedCat extends Cat {}

class Dog extends Animal {}