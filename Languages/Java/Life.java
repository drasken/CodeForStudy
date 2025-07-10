import java.lang.Math;
import java.util.ArrayList;

// Implementing this little Game:
//     - Init board and initializa cells randomply Alive/Dead
//     - Calc each cell the number of neighbours
//     - Calc board next state depending on the previous calc
//     - Init new Board
//     - Pretty print to the terminal



/**
   Class to implement Conway's Game of Life in Java
*/
public class Life{
    
    private int WIDTH;
    public int HEIGTH;
    public int[][] boardState; // Matrix of int representing our world
    private final double CELL_RATIO = 0.75; // This ratio is used to init cells. The higher, more alive cells
    private final String ALIVE = "X";
    private final String DEAD = ".";

    public Life(int width, int height){
	this.WIDTH = width;
	this.HEIGTH = height;
	this.boardState = new int[height][width]; // Initialize the boardState array
	initLife(); // Tested, it works
	//TODO: here implement methods
    }


    /**
       Method that initialize the board.
       Private because should be used inside the constructor
     */
    private void initLife(){
	for(int i = 0; i < this.HEIGTH; i++){
	    for(int j = 0; j < this.HEIGTH; j++){
		double tempRandom = Math.random();
		if(tempRandom > CELL_RATIO){
		    boardState[i][j] = 0;
		} else{
		    boardState[i][j] = 1;
		} 
	    }
	}
    }

    private int getNormalizeIndex(int index, int dimension){
	return (index + dimension) % dimension;
    }

    
    /**
       This method calculate the number of living neighbors for a given cell
     */
    private int calcNeighbor(int[][] matrix, int y_index, int x_index){
	int res = 0;
	for(int i = 0; i < 3; i++){
	    for(int j = 0; j < 3; j++){
		if(i == 1 && j == 1){
		    continue;
			} else{
		    res += matrix[i][j];
		}
	    }
	}
	return res; //TODO: finish implementing it
    }
    

    public String convertToString(int[][] matrix){
	return ""; //TODO: to implement
    }
    

    @Override
    public String toString() {
        return "STUB"; //TODO: use with the convertToString method
    }
    
    public static void main(String[] args){
	Life myLife = new Life(5,5);

	//Test by printing the new board
	for(int[] row: myLife.boardState){
	    for(int el: row){
		System.out.print(el + "");
	    }
	    System.out.println("\n");
	}

	
	
    }
    
}
