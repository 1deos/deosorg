#include "deEvent.h"

#ifdef __cplusplus
extern "C" {
#endif

deEvent *
newEvent(int id)
{   deEvent *ptr = malloc(sizeof(deEvent));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deEvent));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
