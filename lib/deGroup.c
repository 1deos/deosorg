#include "deGroup.h"

#ifdef __cplusplus
extern "C" {
#endif

deGroup *
newGroup(int id)
{   deGroup *ptr = malloc(sizeof(deGroup));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deGroup));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
