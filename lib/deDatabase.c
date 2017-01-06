#include "deDatabase.h"

#ifdef __cplusplus
extern "C" {
#endif

deDatabase *
newDatabase(int id)
{   deDatabase *ptr = malloc(sizeof(deDatabase));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deDatabase));
    ptr->id = id;
    return ptr;
}

#ifdef __cplusplus
}
#endif
