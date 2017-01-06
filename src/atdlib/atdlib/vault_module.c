#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static PyObject *VAULT_ERROR;

static PyObject *vault(PyObject *self, PyObject *args)
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
            PyErr_SetString(VAULT_ERROR, "System command failed");
            return NULL;
        }
        return Py_BuildValue("s", command);
    }
}

static PyMethodDef vault_methods[] = \
{   {   "vault",   vault,   METH_VARARGS,   "Vault"   },
    {   NULL,      NULL,    0,              NULL      },
};

PyMODINIT_FUNC initvault(void)
{   PyObject *module = Py_InitModule("vault", vault_methods);
    if (module != NULL)
    {   VAULT_ERROR = PyErr_NewException("vault.error", NULL, NULL);
        Py_INCREF(VAULT_ERROR);
        PyModule_AddObject(module, "error", VAULT_ERROR);
    }
}

int main(int argc, char *argv[])
{   Py_SetProgramName(argv[0]);
    Py_Initialize();
    initvault();
    return EXIT_SUCCESS;
}
