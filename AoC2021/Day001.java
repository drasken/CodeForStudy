import java.io.*;
import java.util.*;

public class Day001 {
	
    public static void main (String[] args){

	String path = "./input001.txt";
	try (Scanner scanner = new Scanner( new FileReader(path)).useDelimiter("\n")) {

		String line;
		System.out.println(scanner);
	    }
	catch (FileNotFoundException e) {
	    e.printStackTrace();
	}	
    }
}

    
