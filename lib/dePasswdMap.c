#include "dePasswdMap.h"

#ifdef __cplusplus
extern "C" {
#endif

dePasswdMap *
newPasswdMap(int id)
{   dePasswdMap *ptr = malloc(sizeof(dePasswdMap));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(dePasswdMap));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
