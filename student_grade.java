import java.util.Scanner;
public class student_grade {
    public static void main(String[] args){
        // student grade
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter grade : ");
        int grade = sc.nextInt();
        if (grade >= 95 && grade <= 100){
            System.out.print("total : A+");
        }
        else if (grade >= 90 && grade < 95){
            System.out.print("total : A");
        }
        else if (grade >= 85 && grade < 90){
            System.out.print("total : B+");
        }
        else if (grade >= 80 && grade < 85){
            System.out.print("total : B");
        }
        else if (grade >= 70 && grade < 80){
            System.out.print("total : C+");
        }
        else if (grade >= 60 && grade < 70){
            System.out.print("total : C");
        }
        else if (grade >= 50 && grade < 60){
            System.out.print("total : D+");
        }
        else if (grade >= 40 && grade < 50){
            System.out.print("total : D");
        }
        else {
            System.out.print("total : F");
        }
    }
}

