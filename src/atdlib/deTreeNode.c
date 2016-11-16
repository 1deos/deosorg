/* BSD 2-Clause License

Copyright (c) 2013-2016 Andrew T. DeSantis. All rights reserved.
Copyright (c) 2016 DeSantis Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
