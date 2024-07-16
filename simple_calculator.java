import java.util.Scanner;
public class simple_calculator {
    public static void main(String[] args) {
        // Simple calculator
        Scanner sc = new Scanner(System.in);
        System.out.println("Welcome to simple calculator");
        System.out.print("Enter two numbers : ");
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println(x + " + " + y + " = " + (x + y));
        System.out.println(x + " - " + y + " = " + (x - y));
        System.out.println(x + " * " + y + " = " + (x * y));
        System.out.println(x + " / " + y + " = " + (x / y));
    }
}


