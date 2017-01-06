#ifndef __DETREE__
#define __DETREE__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

#include "deTreeNode.h"

typedef struct deTreeObject
{   int size;
    deTreeNode *NIL;
    deTreeNode *root;
} deTree;

extern deTree *newTree(void);
extern void freeTree(deTree *self);
extern void deleteTree(deTree *self, deTreeNode *node);
extern void graphTree(deTree *self, FILE *fp);
extern deTreeNode *insertTree(deTree *self, int value);
extern deTreeNode *maximumTree(deTree *self);
extern deTreeNode *minimumTree(deTree *self);
extern deTreeNode *minimumSubTree(deTree *self, deTreeNode *node);
extern deTreeNode *getTreeNil(deTree *self);
extern deTreeNode *getTreeRoot(deTree *self);
extern int getTreeSize(deTree *self);
extern void setTreeRoot(deTree *self, deTreeNode *node);

#ifdef __cplusplus
}
#endif

#endif /* __DETREE__ */
