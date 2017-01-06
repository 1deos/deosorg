#ifndef __DETREZOR__
#define __DETREZOR__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deTrezorObject
{   int id;
} deTrezor;

extern deTrezor *newTrezor(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DETREZOR__ */
