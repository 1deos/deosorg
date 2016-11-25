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

#include "atdlib.h"

#if ASMJS == TARGET
#define P(s) printf("%s\n", s)
#elif MACOS == TARGET
#define P(s) printf("\x1b[31;01m%s\x1b[0m\n", s)
#endif
#define START 1
#define STOP 2

int
runtime(deOS *this, int cmd) {
#if ASMJS == TARGET
    P("asm.js");
    return EXIT_SUCCESS;
#elif MACOS == TARGET
    if (START == cmd) {
        /*system("clear");*/
        P("Starting ΔOS");
        this = newOS();
        runShell(this);
        return runtime(this, STOP);
    } else if (STOP == cmd) {
        P("Stopping ΔOS");
        freeOS(this);
    }
    return EXIT_SUCCESS;
#else
    return EXIT_FAILURE;
#endif
}

int
main(int argc, char const *argv[])
{   deOS *this = NULL;
    return runtime(this, START);
}
