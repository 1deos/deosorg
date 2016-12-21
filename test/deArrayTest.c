/* Copyright (c) 2013-2016 Andrew T. DeSantis */

#include "atdlib.h"

int main(int argc, char *argv[])
{
    int size;
    deArray(double) *a1;
    a1 = newArray(double);
    freeArray(double, a1);

    deArray(int) *a2;
    a2 = newArray(int);
    appendArray(int, a2, 1);
    appendArray(int, a2, 2);
    size = getArraySize(int, a2);
    printf("%d\n", size);
    freeArray(int, a2);

    deArray(char) *a3;
    a3 = newArray(char);
    appendArray(char, a3, 'a');
    size = getArraySize(char, a3);
    printf("%d\n", size);
    freeArray(char, a3);

    return EXIT_SUCCESS;
}
