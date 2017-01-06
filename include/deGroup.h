#ifndef __DEGROUP__
#define __DEGROUP__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deGroupObject
{   int id;
} deGroup;

extern deGroup *newGroup(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEGROUP__ */
