/*
  Simple toy project to learn better programming in C.  The program
  will get a file name as input, read the file, count the words by
  using space characters and return that number on terminal to user.
*/

#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

#define TEST_FILE_1 "test1_200_w.txt"
#define TEST_FILE_2 "test2_500_w.txt"

int main(int argc, char *argv[]){

  // Check if the input args are 2 as expected. Program name and the
  // file name
  if (argc != 2) {
    fprintf(stderr, "Error. Expected usage: %s <filename>\n", argv[0]);
  }

  // TODO: later add check to ses if input file_name correspond to an
  // existing file

  
}


