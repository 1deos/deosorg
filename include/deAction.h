#ifndef __DEACTION__
#define __DEACTION__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deActionObject
{   int id;
} deAction;

extern deAction *newAction(int id);
extern int freeAction(deAction *self);

#ifdef __cplusplus
}
#endif

#endif /* __DEACTION__ */
