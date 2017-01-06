#ifndef __DEWINDOW__
#define __DEWINDOW__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deWindowObject
{   int id;
} deWindow;

extern deWindow *newWindow(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEWINDOW__ */
