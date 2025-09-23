#include <stdio.h>

// Compile with following code to get shared library
// gcc -shared -o number_cruncher.so -fPIC test.c

int add(int a, int b) {
    return a + b;
}
