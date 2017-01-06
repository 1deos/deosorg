#ifndef __DEEVENT__
#define __DEEVENT__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deEventObject
{   int id;
} deEvent;

extern deEvent *newEvent(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEEVENT__ */
