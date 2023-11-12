import java.io.File;
import java.util.Scanner;

public class Solution_2022_01 {


   public static void main(String[] args) {

        Scanner sc = null;
        int maxCal = 0;

        try {
         sc = new Scanner(new File("2022_01.txt"), "utf-8");
         
         while (sc.hasNextLine()) {
            System.out.println(sc.nextLine());
         }

        } catch (Exception e) {
         e.printStackTrace();
        }
        
        System.out.println(maxCal);
   }

}