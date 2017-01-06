#ifndef __DEMAP__
#define __DEMAP__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deMapObject
{   int id;
} deMap;

extern deMap *newMap(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEMAP__ */
