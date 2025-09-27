package SudokuSolver;

import java.util.Arrays;

public class SudokuSolver{

    private static final int BOARD_SIZE = 9;  //  Single value, assiming square board
    private int[][] board;  // Base board
    private int[][] boardTranspose;  // Useful to check columns
    private int[][] blocks;  // Here saved numberfrom same blocks
    
    /*
      Constructor for base 9x9 table. Assuming a square board
     */
    public SudokuSolver(){

	this.board = new int[BOARD_SIZE][BOARD_SIZE]; // init all el to zero
	this.boardTranspose = this.transpose(this.board);
    }


    // DONE: method to get a transpose matrix
    public int[][] transpose(int[][] board){

	int[][] res = new int[BOARD_SIZE][BOARD_SIZE];
	
	for (int i = 0; i < BOARD_SIZE; i++){
	    for (int j = 0; j < BOARD_SIZE; j++){
		// Here we get original element and we invert position
		res[j][i] = board[i][j];
	    }
	}
	return res;
    }


    // TODO: method to get collection of  


    // TODO: implement a method to read a string and create a table from that
    

    // TODO: make a initRandom method to randomize the board


    // TODO: make a checkIfValid method to check if board is in valid state


    public static void main(String[] args){
	SudokuSolver ssl = new SudokuSolver();
	System.out.println(Arrays.deepToString(ssl.board));
	// Check transpose --> OK
	// ssl.board[1][2] = 999;
	// int [][] test = ssl.transpose(ssl.board);
	// System.out.println(Arrays.deepToString(test));
    }
}
