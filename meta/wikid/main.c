#include <Python.h>
#include <stdio.h>

int
main(int argc, char *argv[])
{
    Py_Initialize();
    #define X(python)\
    PyRun_SimpleString(python);
    #include "python.def"
    Py_Finalize();
    return 0;
}
