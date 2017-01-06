#include "deTreeNode.h"

#ifdef __cplusplus
extern "C" {
#endif

deTreeNode *
newTreeNode(int key)
{   deTreeNode *ptr = malloc(sizeof(deTreeNode));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deTreeNode));
    setTreeNodeKey(ptr, key);
    ptr->parent = NULL;
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

deTreeNode *
newTreeNodeSentinel(void)
{   deTreeNode *ptr = malloc(sizeof(deTreeNode));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deTreeNode));
    ptr->parent = ptr;
    ptr->left = ptr;
    ptr->right = ptr;
    return ptr;
}

void
freeTreeNode(deTreeNode *self)
{   if (self == NULL) return;
    free(self);
}

int
getTreeNodeKey(deTreeNode *self)
{   return self->key;
}

deTreeNode *
getTreeNodeLeft(deTreeNode *self)
{   return self->left;
}

deTreeNode *
getTreeNodeParent(deTreeNode *self)
{   return self->parent;
}

deTreeNode *
getTreeNodeRight(deTreeNode *self)
{   return self->right;
}

int
setTreeNodeKey(deTreeNode *self, int key)
{   int old_key;
    old_key = self->key;
    self->key = key;
    return old_key;
}

void
setTreeNodeParent(deTreeNode *self, deTreeNode *parent)
{   self->parent = parent;
}

void
setTreeNodeLeft(deTreeNode *self, deTreeNode *child)
{   self->left = child;
}

void
setTreeNodeRight(deTreeNode *self, deTreeNode *child)
{   self->right = child;
}

#ifdef __cplusplus
}
#endif
