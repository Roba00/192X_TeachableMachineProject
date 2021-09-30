package BirdDataset;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.Random;
import org.apache.commons.io.FileUtils;

/**
 * @author Roba Abbajabal
 */
public class RandomImgSelection {
	
	final static String[] CLASS_NAMES = {"0_AFRICAN FIREFINCH", 
			"1_ALEXANDRINE PARAKEET", "2_AMERICAN GOLDFINCH",
			"3_BALTIMORE ORIOLE", "4_BEARDED BELLBIRD", "5_BORNEAN LEAFBIRD"};
	final static String[] SET_NAMES = {"Set1", "Set2", "Set3", "Set4", 
			"Set5", "Set6", "Set7"};
	final static String[] PERCENT_NAMES = {"20%", "40%", "60%", "80%", "100%"};
	
	public static void main(String args[]) 
	{
		Scanner scan = new Scanner(System.in);
		HashSet<Integer> elements = new HashSet<Integer>();
		Random rand = new Random(0);
		
		System.out.print("Source folder path: ");
		String filePathStr = scan.nextLine();
		System.out.print("Destination folder path: ");
		String fileDestStr = scan.nextLine();
		
		for (int percentI = 0; percentI < PERCENT_NAMES.length; percentI++)
		{
			for (int setI = 0; setI < SET_NAMES.length; setI++)
			{
				rand.setSeed(setI*100); //Sets seed to set
				System.out.println(setI + " " + PERCENT_NAMES[percentI]);
				
				int numRandomized = chooseNumRandomized(percentI);
				
				elements = new HashSet<Integer>();
				while (elements.size() < numRandomized) {
					elements.add(rand.nextInt(100));
				}

				Integer[] elementsArr = elements.toArray(new Integer[elements.size()]);
				
				for (int classI = 0; classI < CLASS_NAMES.length; classI++)
				{
					for (int i = 0; i < numRandomized; i++) 
					{
						int numDigits = String.valueOf(elementsArr[i]+1).length();
						try {

							//System.out.println(chooseFile((elementsArr[i]+1), numDigits, filePathStr, classI));
							//System.out.println(new File(fileDestStr + "\\" + PERCENT_NAMES[percentI] + "\\" + 
							//		SET_NAMES[setI] + "\\" + CLASS_NAMES[classI] + "\\" + (elementsArr[i]+1) + ".jpg"));
							
							FileUtils.copyFile(chooseFile((elementsArr[i]+1), numDigits, filePathStr, classI), 
									new File(fileDestStr + "\\" + PERCENT_NAMES[percentI] + "\\" + 
									SET_NAMES[setI] + "\\" + CLASS_NAMES[classI] + "\\" + (elementsArr[i]+1) + ".jpg"));;
						}
						catch (IOException e) {
							System.out.println("File path or file name not named correctly. Exiting . . .");
							System.exit(-1);
						}
					}
				}
			}
		}
		System.out.println("Images selected successfully.");
		scan.close();
	}
	
	static int chooseNumRandomized(int percentIndex)
	{
		switch (percentIndex)
		{
			case 0:
				return 20;
			case 1:
				return 40;
			case 2:
				return 60;
			case 3:
				return 80;
			case 4:
				return 100;
			default:
				throw new IllegalArgumentException("Integer "
						+ "must have a percent index greater than -1 and less than 5.");
		}
	}
	
	static File chooseFile(int integer, int numDigits, String filePathStr, int classI) {
		switch (numDigits) {
			case 1:
				return new File(filePathStr + "\\" + CLASS_NAMES[classI] + "\\" +"\\00"  + integer + ".jpg");
			case 2:
				return new File(filePathStr + "\\" + CLASS_NAMES[classI] + "\\0"  + integer + ".jpg");
			case 3:
				return new File(filePathStr + "\\" + CLASS_NAMES[classI] + "\\" + integer + ".jpg");
			default:
				throw new IllegalArgumentException("Integer "
				+ "must have a number of digits greater than 0 and less than 4.");
		}
	}
}
