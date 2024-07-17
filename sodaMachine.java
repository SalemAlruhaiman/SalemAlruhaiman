import java.util.Scanner;
public class sodaMachine {
    // global variables
    static String[] sodaList = {"CocaCola", "Pepsi   ", "7up     ", "Fanta   ", "Mirinda ", "Sprite  "}; // 8-length for each element
    static double[] priceList = {2.5, 2.75, 2.25, 4, 2, 3};
    static double[] caloryList = {70.8, 60.3, 72.3, 66.5, 67.9, 71.1};
    static boolean check_lengths = (sodaList.length == priceList.length) && (sodaList.length == caloryList.length) && (priceList.length == caloryList.length);

    public static void menu(){
        // Display the Menu
        if (check_lengths){
            System.out.println("===============================================");
            System.out.println("Product No. \t Product \t Price \t   Calories");
            System.out.println("===============================================");
            for (int i=0; i < sodaList.length; i++){
                System.out.println((i+1) + " -------------- " + sodaList[i] + "\t  " + priceList[i] + "\t     " + caloryList[i]);
            }

        } else {
            System.out.println("length error!");
        }
    }
    public static void main(String[] args) {
        // Soda Machine
        double credit = 50;
        Scanner sc = new Scanner(System.in);
        System.out.println("Credit: " + credit);

        // display the menu
        menu();

        // purchase process
        System.out.print("\nSelect your choice: ");
        int choice = sc.nextInt();
        System.out.print("Quantity: ");
        int quantity = sc.nextInt();
        double total = quantity * priceList[choice-1];
        double change = credit - total;

        // check order
        if (quantity <= 0){
            System.out.println("Invalid Quantity!");
        } else {
            switch (choice){
                case 1:
                    if (credit >= total){
                        System.out.println("Done!\n");
                        System.out.println("bill:");
                        System.out.println("Product Number: " + choice);
                        System.out.println("Product Name: " + sodaList[choice-1]);
                        System.out.println("Product Price: " + priceList[choice-1]);
                        System.out.println("Product Calories: " + caloryList[choice-1]);
                        System.out.println("Total Price: " + total);
                        System.out.println("Change: " + change);
                    } else {
                        System.out.println("Invalid Quantity!");
                    }
                    break;
                case 2:
                    if (credit >= total){
                        System.out.println("Done!\n");
                        System.out.println("bill:");
                        System.out.println("Product Number: " + choice);
                        System.out.println("Product Name: " + sodaList[choice-1]);
                        System.out.println("Product Price: " + priceList[choice-1]);
                        System.out.println("Product Calories: " + caloryList[choice-1]);
                        System.out.println("Total Price: " + total);
                        System.out.println("Change: " + change);
                    } else {
                        System.out.println("Invalid Quantity!");
                    }
                    break;
                case 3:
                    if (credit >= total){
                        System.out.println("Done!\n");
                        System.out.println("bill:");
                        System.out.println("Product Number: " + choice);
                        System.out.println("Product Name: " + sodaList[choice-1]);
                        System.out.println("Product Price: " + priceList[choice-1]);
                        System.out.println("Product Calories: " + caloryList[choice-1]);
                        System.out.println("Total Price: " + total);
                        System.out.println("Change: " + change);
                    } else {
                        System.out.println("Invalid Quantity!");
                    }
                    break;
                case 4:
                    if (credit >= total){
                        System.out.println("Done!\n");
                        System.out.println("bill:");
                        System.out.println("Product Number: " + choice);
                        System.out.println("Product Name: " + sodaList[choice-1]);
                        System.out.println("Product Price: " + priceList[choice-1]);
                        System.out.println("Product Calories: " + caloryList[choice-1]);
                        System.out.println("Total Price: " + total);
                        System.out.println("Change: " + change);
                    } else {
                        System.out.println("Invalid Quantity!");
                    }
                    break;
                case 5:
                    if (credit >= total){
                        System.out.println("Done!\n");
                        System.out.println("bill:");
                        System.out.println("Product Number: " + choice);
                        System.out.println("Product Name: " + sodaList[choice-1]);
                        System.out.println("Product Price: " + priceList[choice-1]);
                        System.out.println("Product Calories: " + caloryList[choice-1]);
                        System.out.println("Total Price: " + total);
                        System.out.println("Change: " + change);
                    } else {
                        System.out.println("Invalid Quantity!");
                    }
                    break;
                case 6:
                    if (credit >= total){
                        System.out.println("Done!\n");
                        System.out.println("bill:");
                        System.out.println("Product Number: " + choice);
                        System.out.println("Product Name: " + sodaList[choice-1]);
                        System.out.println("Product Price: " + priceList[choice-1]);
                        System.out.println("Product Calories: " + caloryList[choice-1]);
                        System.out.println("Total Price: " + total);
                        System.out.println("Change: " + change);
                    } else {
                        System.out.println("Invalid Quantity!");
                    }
                    break;
                default:
                    System.out.println("Invalid choice!");
                    break;
            }
        }
    }
}