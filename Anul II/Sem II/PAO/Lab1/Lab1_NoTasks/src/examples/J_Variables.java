package examples;

/**
 * Created by bogdan pahontu
 * Variables Scope
 */
public class J_Variables {
    public static void main(String args[]){

    }

    public void eatIfHungry(boolean hungry) {
        if (hungry) {
            int bitesOfCheese = 1;
        } // bitesOfCheese goes out of scope here
        //System.out.println(bitesOfCheese);// DOES NOT COMPILE
    }

    public void eatIfHungry2(boolean hungry) {
        if (hungry) {
            int bitesOfCheese = 1;
            //System.out.println(nrMeals);
            {
                boolean teenyBit = true;
                System.out.println(bitesOfCheese);
            }
        }
        int nrMeals;
        //System.out.println(teenyBit); // DOES NOT COMPILE
    }
}
