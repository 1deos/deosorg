#include "deTrezor.h"

#ifdef __cplusplus
extern "C" {
#endif

deTrezor *
newTrezor(int id)
{   deTrezor *ptr = malloc(sizeof(deTrezor));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deTrezor));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
