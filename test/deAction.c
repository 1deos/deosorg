#include "atdlib.h"

static int
testCreateAndFreeAction(void)
{   int res = 0;
    deAction *action = newAction(123);
    if (123 == action->id)
        res = 1;
    res = freeAction(action);
    return res;
}

int
main(int argc, char const *argv[])
{   int test = 0;
    test += testCreateAndFreeAction();
    printf("%d\n",test);
    return EXIT_SUCCESS;
}
