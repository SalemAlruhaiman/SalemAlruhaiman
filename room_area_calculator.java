import java.util.Scanner;
public class room_area_calculator {
    public static void main(String[] args){
        // area calculator
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the area of the room : ");
        double x = sc.nextInt();
        double y = sc.nextInt();
        double area = x * y;
        System.out.println("The area of the room is " + area);
    }
}

