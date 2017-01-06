#ifndef __DELISTNODE__
#define __DELISTNODE__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deListNodeObject
{   int key;
    struct deListNodeObject *next;
    struct deListNodeObject *prev;
} deListNode;

extern deListNode *newListNode(int key);
extern deListNode *newListNodeSentinel(void);
extern void freeListNode(deListNode *ptr);
extern int getListNodeKey(deListNode *ptr);
extern deListNode *getListNodeNext(deListNode *ptr);
extern deListNode *getListNodePrev(deListNode *ptr);
extern int setListNodeKey(deListNode *ptr, int key);

#ifdef __cplusplus
}
#endif

#endif /* __DELISTNODE__ */
