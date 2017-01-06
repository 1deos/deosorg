#include "dePasswd.h"

#ifdef __cplusplus
extern "C" {
#endif

dePasswd *
newPasswd(int id)
{   dePasswd *ptr = malloc(sizeof(dePasswd));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(dePasswd));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
