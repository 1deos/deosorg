#include "deGroupMenu.h"

#ifdef __cplusplus
extern "C" {
#endif

deGroupMenu *
newGroupMenu(int id)
{   deGroupMenu *ptr = malloc(sizeof(deGroupMenu));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deGroupMenu));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
