#ifndef __DEVAULT__
#define __DEVAULT__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deVaultObject
{   int id;
} deVault;

extern deVault *newVault(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEVAULT__ */
