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
