package SudokuSolver.src.sudoku;

public class Board{

    private int[][] board;
    private int size = 9;  // here assuming a standard 9x9 board

    /**
       This is the basic constructor for an empty board.
       All call values are initialized to 0
     */
    public Board(){
	for(int i = 0; i < this.size; i++){
	    for(int j = 0; j < this.size; j++){
		this.board[i][j] = 0;
	    }
	}
    }

    @Override
    public String toString(){
	return "STUB";  // Need to implement
    }
}
