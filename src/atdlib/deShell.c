/* BSD 2-Clause License

Copyright (c) 2013-2016 Andrew T. DeSantis. All rights reserved.
Copyright (c) 2016 DeSantis Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#include "deShell.h"

#ifdef __cplusplus
extern "C" {
#endif

static int _read(void);
static char *_eval(int in);
static int _print(deOS *os, char *out);
static void _printMainMenu(void);
static void _printIn(int count);
static void _printOut(int count, char *out);

deShell *
newShell(deOS *os)
{   deShell *shell = (deShell *) malloc(sizeof(deShell));
    if (shell == NULL) return NULL;
    memset(shell, 0, sizeof(deShell));
    shell->count = 0;
    shell->os = os;
    setOSShell(os, shell);
    shell->self = newObject(TYPE_SHELL);
    if (getShellType(shell) != TYPE_SHELL)
    {   freeShell(shell);
        return NULL;
    }
    return shell;
}

int
freeShell(deShell *shell)
{   if (NULL == shell) return -1;
    if (NULL != shell->self)
        freeObject(shell->self);
    free(shell);
    return 0;
}

int
incrementShellCount(deShell *shell)
{   if (NULL == shell) return -1;
    shell->count += 1;
    return getShellCount(shell);
}

int
runShell(deOS *os)
{   newShell(os);
    int loop = 1;
    while (loop > 0)
    {   if (0 == getShellCount(os->shell))
        {   _printMainMenu();
            incrementShellCount(os->shell);
            _printIn(getShellCount(os->shell));
        }
        loop = _print(os, _eval(_read()));
    }
    return EXIT_SUCCESS;
}

int
getShellCount(deShell *shell)
{   if (NULL == shell) return -1;
    return shell->count;
}

deOS *getShellOS(deShell *shell)
{   if (NULL == shell) return NULL;
    if (NULL == shell->os) return NULL;
    return shell->os;
}

int getShellType(deShell *shell)
{   if (NULL == shell) return -1;
    if (NULL == shell->self) return -2;
    int type = getObjectType(shell->self);
    return type;
}

static int
_read(void)
{   int in;
    scanf("%d", &in);
    return in;
}

static char *
_eval(int in)
{   if (1 == in)
        return "1";
    else
        return "0";
}

static int
_print(deOS *os, char *out)
{   _printOut(getShellCount(os->shell), out);
    incrementShellCount(os->shell);
    _printIn(getShellCount(os->shell));
    return 1;
}

static void
_printMainMenu(void)
{	printf("Main Menu\n");
}

static void
_printIn(int count)
{	printf("\nIn [\x1b[36;01m%d\x1b[0m]: ", count);
}

static void
_printOut(int count, char *out)
{	printf("\x1b[31;01mOut[\x1b[36;01m%d\x1b[31;01m]: \x1b[0m%s\x1b[0m\n",
           count,
           out);
}

#ifdef __cplusplus
}
#endif
