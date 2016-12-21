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
