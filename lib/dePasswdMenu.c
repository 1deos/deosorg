#include "dePasswdMenu.h"

#ifdef __cplusplus
extern "C" {
#endif

dePasswdMenu *
newPasswdMenu(int id)
{   dePasswdMenu *ptr = malloc(sizeof(dePasswdMenu));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(dePasswdMenu));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
