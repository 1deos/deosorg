#include "deMenu.h"

#ifdef __cplusplus
extern "C" {
#endif

deMenu *
newMenu(int id)
{   deMenu *ptr = malloc(sizeof(deMenu));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deMenu));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
