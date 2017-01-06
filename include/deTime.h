#ifndef __DETIME__
#define __DETIME__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deTimeObject
{   int id;
} deTime;

extern deTime *newTime(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DETIME__ */
