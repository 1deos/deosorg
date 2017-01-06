#include "deMap.h"

#ifdef __cplusplus
extern "C" {
#endif

deMap *
newMap(int id)
{   deMap *ptr = malloc(sizeof(deMap));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deMap));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
