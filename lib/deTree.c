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
