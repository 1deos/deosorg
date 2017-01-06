#include "deBackup.h"

#ifdef __cplusplus
extern "C" {
#endif

deBackup *
newBackup(int id)
{   deBackup *ptr = malloc(sizeof(deBackup));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deBackup));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
