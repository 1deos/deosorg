#ifndef __DEPASSWD__
#define __DEPASSWD__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct dePasswdObject
{   int id;
} dePasswd;

extern dePasswd *newPasswd(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEPASSWD__ */
