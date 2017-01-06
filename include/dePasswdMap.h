#ifndef __DEPASSWDMAP__
#define __DEPASSWDMAP__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct dePasswdMapObject
{   int id;
} dePasswdMap;

extern dePasswdMap *newPasswdMap(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEPASSWDMAP__ */
