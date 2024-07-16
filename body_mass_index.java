import java.util.Scanner;
public class body_mass_index {
    public static void main(String[] args){
        // body mass index BMI
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your height: ");
        double height = sc.nextDouble();
        System.out.println("Enter your weight:");
        double weight = sc.nextDouble();
        double bmi = weight / (height * height);

        if (bmi < 18.5){
            System.out.println("You are Underweight");
        }
        else if (bmi >= 18.5 && bmi <= 24.9){
            System.out.println("You are Normal Weight");
        }
        else if (bmi >= 25 && bmi <= 29.9){
            System.out.println("You are Overweight");
        }
        else {
            System.out.println("You are Obase");
        }
    }
}

