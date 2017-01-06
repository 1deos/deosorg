#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static PyObject *DEOS_ERROR;

static PyObject *deos(PyObject *self, PyObject *args)
{   const char *command;
    if (!PyArg_ParseTuple(args, "s", &command))
    {   return NULL;    
    } else {
        char filename[1000], line[10000];
        FILE *file = popen(filename, "r");
        if (file)
        {   while (NULL != fgets(line, sizeof(line), file))
            {   printf("%s\n", line);
            }
            pclose(file);
        } else {
            PyErr_SetString(DEOS_ERROR, "System command failed");
            return NULL;
        }
        return Py_BuildValue("s", command);
    }
}

static PyMethodDef deos_methods[] = \
{   {   "deos",   deos,   METH_VARARGS,   "DeOS"   },
    {   NULL,     NULL,   0,              NULL     },
};

static void _init_deos(void)
{   PyObject *module = Py_InitModule("deos", deos_methods);
    if (module != NULL)
    {   DEOS_ERROR = PyErr_NewException("deos.error", NULL, NULL);
        Py_INCREF(DEOS_ERROR);
        PyModule_AddObject(module, "error", DEOS_ERROR);
    }
}

PyMODINIT_FUNC initdeos(void)
{   _init_deos();
}

int main(int argc, char *argv[])
{   Py_SetProgramName(argv[0]);
    Py_Initialize();
    initdeos();
    return EXIT_SUCCESS;
}
