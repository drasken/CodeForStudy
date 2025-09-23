/*
mylib.c
compile it in a shared library using command:
gcc -shared -o mylib.so -fPIC mylib.c
*/

#include <stdio.h>

void hello() {
    printf("Hello from C!\n");
}

int add(int a, int b) {
    return a + b;
}
