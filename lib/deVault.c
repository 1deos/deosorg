#include "deVault.h"

#ifdef __cplusplus
extern "C" {
#endif

deVault *
newVault(int id)
{   deVault *ptr = malloc(sizeof(deVault));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deVault));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
