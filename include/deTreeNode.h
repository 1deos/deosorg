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
