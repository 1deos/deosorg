#ifndef __DEWALLET__
#define __DEWALLET__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deWalletObject
{   int id;
} deWallet;

extern deWallet *newWallet(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEWALLET__ */
