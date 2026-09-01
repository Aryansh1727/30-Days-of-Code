import java.io.*;
import java.util.*;

public class Day21_Generics {
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read integer array
        int n = sc.nextInt();
        Integer[] intArray = new Integer[n];

        for (int i = 0; i < n; i++) {
            intArray[i] = sc.nextInt();
        }
        
        // Read string array
        int m = sc.nextInt();
        String[] stringArray = new String[m];

        for (int i = 0; i < m; i++) {
            stringArray[i] = sc.next();
        }
        
        // Print both arrays using the same generic method
        printArray(intArray);
        printArray(stringArray);

        sc.close();
    }
}
