#ifndef __DELIST__
#define __DELIST__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

#include "deListNode.h"

typedef struct deListObject
{   int size;
    deListNode *sentinel;
} deList;

extern deList *newList(void);
extern void freeList(deList *list);
extern int appendList(deList *ptr, int value);
extern void deleteList(deList *lst, deListNode *n);
extern void graphList(deList *list, FILE *fp);
extern int prependList(deList *ptr, int value);
extern int searchList(deList *ptr, int value);
extern int getListSize(deList *ptr);
extern deListNode *getListHead(deList *ptr);
extern deListNode *getListTail(deList *ptr);
extern deListNode *getListSentinel(deList *ptr);

#ifdef __cplusplus
}
#endif

#endif /* __DELIST__ */
