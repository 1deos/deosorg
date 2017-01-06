#ifndef __DEDATABASE__
#define __DEDATABASE__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deDatabaseObject
{   int id;
} deDatabase;

extern deDatabase *newDatabase(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEDATABASE__ */
