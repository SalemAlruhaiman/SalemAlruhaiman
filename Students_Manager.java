import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Students_Manager {
    public static void add_Students(ArrayList<String> nameList, ArrayList<Double> gradeList){
        // Adding New Students And Grades
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter student name: ");
        String newName = sc.nextLine();
        System.out.print("Enter student grade: ");
        double newGrade = sc.nextDouble();

        // Adding new student and grade
        nameList.add(newName);
        gradeList.add(newGrade);

        System.out.println("Student and grade added successfully.");
    }

    public static void display_Students(ArrayList<String> names, ArrayList<Double> grades){
        // Displaying Students Names And Grades
        for (int i = 0; i < names.size(); i++){
            System.out.println(names.get(i) + ": " + grades.get(i));
        }
    }

    public static double average(ArrayList<Double> grades) throws IllegalArgumentException {
        // Calculating the average of Students Grades
        if (grades.size() == 0) {
            throw new IllegalArgumentException("No grades available to calculate average.");
        }

        double sum = 0;
        for (double grade : grades) {
            sum += grade;
        }
        return sum / grades.size();
    }

    public static void main(String[] args){
        // Students Manager
        ArrayList<String> students = new ArrayList<>(Arrays.asList("Salem", "Fahad", "Renad", "Raghad"));
        ArrayList<Double> grades = new ArrayList<>(Arrays.asList(99.2, 99.0, 94.43, 99.9));

        // Displaying students
        System.out.println("Current students:");
        display_Students(students, grades);

        // Adding a new student
        add_Students(students, grades);

        // Displaying students after addition
        System.out.println("Students after addition:");
        display_Students(students, grades);

        // Calculating and displaying the average grade
        try {
            double avg = average(grades);
            System.out.println("Average grade: " + avg);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
