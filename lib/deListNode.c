#include "deListNode.h"

#ifdef __cplusplus
extern "C" {
#endif

deListNode *
newListNode(int key)
{   /* create deListNode pointer */
    deListNode *ptr = malloc(sizeof(deListNode));
    /* confirm pointer creation */
    if (ptr == NULL) return NULL;
    /* fill memory with a constant byte */
    memset(ptr, 0, sizeof(deListNode));
    /* set member values */
    setListNodeKey(ptr, key);
    ptr->next = NULL;
    ptr->prev = NULL;
    /* return pointer */
    return ptr;
}

deListNode *
newListNodeSentinel(void)
{   /* create deListNode pointer */
    deListNode *ptr = malloc(sizeof(deListNode));
    /* confirm pointer creation */
    if (ptr == NULL) return NULL;
    /* fill memory with a constant byte */
    memset(ptr, 0, sizeof(deListNode));
    /* set member values */
    ptr->next = ptr;
    ptr->prev = ptr;
    /* return pointer */
    return ptr;
}

void
freeListNode(deListNode *ptr)
{   if (ptr == NULL) return;
    free(ptr);
}

int
getListNodeKey(deListNode *ptr)
{   return ptr->key;
}

deListNode *
getListNodeNext(deListNode *ptr)
{   return ptr->next;
}

deListNode *
getListNodePrev(deListNode *ptr)
{   return ptr->prev;
}

int
setListNodeKey(deListNode *ptr, int key)
{   int old_key = ptr->key;
    ptr->key = key;
    return old_key;
}

#ifdef __cplusplus
}
#endif
