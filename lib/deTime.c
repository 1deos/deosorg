#include "deTime.h"

#ifdef __cplusplus
extern "C" {
#endif

deTime *
newTime(int id)
{   deTime *ptr = malloc(sizeof(deTime));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deTime));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
