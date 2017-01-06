#ifndef __DETREENODE__
#define __DETREENODE__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deTreeNodeObject
{   int key;
    struct deTreeNodeObject *parent;
    struct deTreeNodeObject *left;
    struct deTreeNodeObject *right;
} deTreeNode;

extern deTreeNode *newTreeNode(int key);
extern deTreeNode *newTreeNodeSentinel(void);
extern void freeTreeNode(deTreeNode *self);
extern int getTreeNodeKey(deTreeNode *self);
extern deTreeNode *getTreeNodeLeft(deTreeNode *self);
extern deTreeNode *getTreeNodeParent(deTreeNode *self);
extern deTreeNode *getTreeNodeRight(deTreeNode *self);
extern int setTreeNodeKey(deTreeNode *self, int key);
extern void setTreeNodeParent(deTreeNode *self, deTreeNode *parent);
extern void setTreeNodeLeft(deTreeNode *self, deTreeNode *child);
extern void setTreeNodeRight(deTreeNode *self, deTreeNode *child);

#ifdef __cplusplus
}
#endif

#endif /* __DETREENODE__ */
