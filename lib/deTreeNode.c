/* ΔOS: Decentralized Operating System

Copyright (c) 2013-2017 Andrew DeSantis <atd@gmx.it>
Copyright (c) 2016-2017 DeSantis Inc. <inc@gmx.it>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

This file incorporates work covered by the BSD 2-Clause License,
as well as the following copyright, and permission notice:
---
ΔOS may be used and distributed under the terms of the GPLv3,
which are available at: <http://www.gnu.org/licenses/gpl-3.0.html>

If you would like to embed ΔOS within a commercial application or
redistribute it in a modified binary form, contact DeSantis Inc.
*/

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
