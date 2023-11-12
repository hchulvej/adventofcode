import java.io.File;
import java.util.Scanner;

public class Solution_2022_01 {

   public static void main(String[] args) {

      Scanner sc = null;
      int maxCal = 0;

      try {
         sc = new Scanner(new File("2022_01.txt"), "utf-8");
         int elfLoad = 0;
         while (sc.hasNextLine()) {
            String line = sc.nextLine();

            if (line.length() == 0) {
               if (elfLoad > maxCal) {
                  maxCal = elfLoad;
               }
               elfLoad = 0;
            } else {
               elfLoad += Integer.parseInt(line);
            }
         }

      } catch (Exception e) {
         e.printStackTrace();
      }

      System.out.println(maxCal);
   }

}