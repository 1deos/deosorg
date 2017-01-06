#include "deWindow.h"

#ifdef __cplusplus
extern "C" {
#endif

deWindow *
newWindow(int id)
{   deWindow *ptr = malloc(sizeof(deWindow));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deWindow));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
