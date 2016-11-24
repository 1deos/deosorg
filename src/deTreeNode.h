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
