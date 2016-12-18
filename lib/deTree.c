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

  Copyright (c) 2013-2017 Andrew DeSantis. All rights reserved.
  Copyright (c) 2016-2017 DeSantis Inc. All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:

  * Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
  COPYRIGHT HOLDER COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
  OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
  BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
  OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

ΔOS may be used and distributed under the terms of the GPLv3,
which are available at: <http://www.gnu.org/licenses/gpl-3.0.html>

If you would like to embed ΔOS within a commercial application or
redistribute it in a modified binary form, contact DeSantis Inc.
*/

#include "deTree.h"

#ifdef __cplusplus
extern "C" {
#endif

static void _decrementTreeSize(deTree *self);
static void _freeTree(deTreeNode *node,
                      deTreeNode *NIL);
static void _graphTree(deTree *self,
                       deTreeNode *node,
                       FILE *fp);
static void _incrementTreeSize(deTree *self);
static void _initTreeNil(deTree *self);
static void _initTreeRoot(deTree *self);
static void _initTreeSize(deTree *self);
static void _transplantTree(deTree *self,
                            deTreeNode *u,
                            deTreeNode *v);

deTree *
newTree(void)
{   deTree *self = (deTree *) malloc(sizeof(deTree));
    if (self == NULL) return NULL;
    memset(self, 0, sizeof(deTree));
    _initTreeNil(self);
    _initTreeRoot(self);
    _initTreeSize(self);
    return self;
}

void
freeTree(deTree *self)
{   if (self == NULL) return;
    deTreeNode *NIL = getTreeNil(self);
    deTreeNode *root = getTreeRoot(self);
    _freeTree(root, NIL);
    free(NIL);
    free(self);
}

void
deleteTree(deTree *self, deTreeNode *node)
{   deTreeNode *NIL;
    NIL = getTreeNil(self);
    /* node has no left children */
    if (getTreeNodeLeft(node) == NIL)
        _transplantTree(self, node, getTreeNodeRight(node));
    /* node has left, but no right children */
    else if (getTreeNodeRight(node) == NIL)
        _transplantTree(self, node, getTreeNodeLeft(node));
    else /* the successor of node */
    {   deTreeNode *min = minimumSubTree(self, getTreeNodeRight(node));
        if (getTreeNodeParent(min) != node)
        {   _transplantTree(self, min, getTreeNodeRight(min));
            setTreeNodeRight(min, getTreeNodeRight(node));
            setTreeNodeParent(getTreeNodeRight(min), min);
        }
        _transplantTree(self, node, min);
        setTreeNodeLeft(min, getTreeNodeLeft(node));
        setTreeNodeParent(getTreeNodeLeft(min), min);
        if (getTreeRoot(self) == node) setTreeRoot(self, min);
    }
    freeTreeNode(node);
    _decrementTreeSize(self);
}

void
graphTree(deTree *self, FILE *fp)
{  /* Create dot graph using a recursive algorithm,
    * called an inorder tree walk.
    */
    fprintf(fp, "digraph deTree {\n");
    fprintf(fp, "    node [fontname=\"Arial\"];\n");
    _graphTree(self, getTreeRoot(self), fp);
    fprintf(fp, "}");
}

deTreeNode *
insertTree(deTree *self, int value)
{  /* Begins at the root of the tree and the i pointer
    * traces a simple path downard looking for a NIL
    * to replace with the input value.
    *
    * We maintain a trailing pointer as a parent of i.
    *
    * After initialization the while loop causes these
    * two pointers to move down the tree, going left
    * or right depending on the comparison of i.key
    * and node.key until i becomes NIL.
    *
    * We need the trailing pointer, because by the time
    * we have trailing pointer, because by the time we
    * have found the NIL the search has proceeded one
    * step beyond the node that needs to be changed.
    */
    deTreeNode *NIL, *trailing, *root, *i, *node;
    NIL = getTreeNil(self);
    root = getTreeRoot(self);
    node = newTreeNode(value);
    setTreeNodeLeft(node, NIL);
    setTreeNodeRight(node, NIL);
    trailing = NIL;
    i = root;
    while (i != NIL)
    {   trailing = i;
        if (getTreeNodeKey(node) < getTreeNodeKey(i))
            i = getTreeNodeLeft(i);
        else i = getTreeNodeRight(i);
    }
    setTreeNodeParent(node, trailing);
    if (trailing == NIL) setTreeRoot(self, node);
    else if (getTreeNodeKey(node) < getTreeNodeKey(trailing))
        setTreeNodeLeft(trailing, node);
    else setTreeNodeRight(trailing, node);
    _incrementTreeSize(self);
    return node;
}

deTreeNode *
maximumTree(deTree *self)
{  /* Returns the pointer to a tree's maximum
    * element.
    */
    deTreeNode *NIL, *node;
    NIL = getTreeNil(self);
    node = getTreeRoot(self);
    while (getTreeNodeRight(node) != NIL)
        node = getTreeNodeRight(node);
    return node;
}

deTreeNode *
minimumTree(deTree *self)
{  /* Returns the pointer to a tree's minimum
    * element.
    */
    deTreeNode *NIL, *node;
    NIL = getTreeNil(self);
    node = getTreeRoot(self);
    while (getTreeNodeLeft(node) != NIL)
        node = getTreeNodeLeft(node);
    return node;
}

deTreeNode *
minimumSubTree(deTree *self, deTreeNode *node)
{  /* Returns the pointer to the minimum element
    * in the subtree rooted at a given node.
    */
    deTreeNode *NIL;
    NIL = getTreeNil(self);
    while (getTreeNodeLeft(node) != NIL)
        node = getTreeNodeLeft(node);
    return node;
}

deTreeNode *
getTreeNil(deTree *self)
{  /* Returns the tree's NIL node. If self->NIL
    * does not yet exist we initalize it.
    */
    if (self->NIL == NULL) _initTreeNil(self);
    return self->NIL;
}

deTreeNode *
getTreeRoot(deTree *self)
{  /* Returns a pointer to the root node of
    * a tree.
    */
    return self->root;}

int
getTreeSize(deTree *self)
{  /* Returns the total number of nodes in the
    * tree as an integer.
    */
    return self->size;
}

void
setTreeRoot(deTree *self, deTreeNode *node)
{  /* Sets the tree's root pointer to node.
    */
    self->root = node;
}

static void
_decrementTreeSize(deTree *self)
{   self->size -= 1;
}

static void
_freeTree(deTreeNode *node, deTreeNode *NIL)
{   if (node != NIL)
    {   _freeTree(getTreeNodeLeft(node), NIL);
        _freeTree(getTreeNodeRight(node), NIL);
        free(node);
    }
}

static void
_graphTree(deTree *self, deTreeNode *node, FILE *fp)
{   deTreeNode *NIL;
    NIL = getTreeNil(self);
    if (node != NIL)
    {   _graphTree(self, getTreeNodeLeft(node), fp);
        fprintf(fp, "    node [style=filled,fillcolor=white];\n");
        if (getTreeNodeLeft(node) != NIL)
            fprintf(fp, "    %d -> %d;\n",
                    getTreeNodeKey(node),
                    getTreeNodeKey(getTreeNodeLeft(node)));
        if (getTreeNodeRight(node) != NIL)
            fprintf(fp, "    %d -> %d;\n",
                    getTreeNodeKey(node),
                    getTreeNodeKey(getTreeNodeRight(node)));
        _graphTree(self, getTreeNodeRight(node), fp);
    }
}

static void
_incrementTreeSize(deTree *self)
{   self->size += 1;
}

static void
_initTreeNil(deTree *self)
{   deTreeNode *NIL;
    NIL = newTreeNodeSentinel();
    self->NIL = NIL;
}

static void
_initTreeRoot(deTree *self)
{   if (self->NIL == NULL) _initTreeNil(self);
    setTreeRoot(self, self->NIL);
}

static void
_initTreeSize(deTree *self)
{   self->size = 0;
}

static void
_transplantTree(deTree *self, deTreeNode *u, deTreeNode *v)
{   deTreeNode *NIL = getTreeNil(self);
    if (u == getTreeRoot(self)) setTreeRoot(self, v);
    else if (u == getTreeNodeLeft(getTreeNodeParent(u)))
        setTreeNodeLeft(getTreeNodeParent(u), v);
    else setTreeNodeRight(getTreeNodeParent(u), v);
    if (v != NIL) setTreeNodeParent(v, getTreeNodeParent(u));
}

#ifdef __cplusplus
}
#endif
