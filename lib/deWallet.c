#include "deWallet.h"

#ifdef __cplusplus
extern "C" {
#endif

deWallet *
newWallet(int id)
{   deWallet *ptr = malloc(sizeof(deWallet));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deWallet));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
