#include "deSettings.h"

#ifdef __cplusplus
extern "C" {
#endif

deSettings *
newSettings(int id)
{   deSettings *ptr = malloc(sizeof(deSettings));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deSettings));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
