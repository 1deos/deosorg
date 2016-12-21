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

#include "deList.h"

#ifdef __cplusplus
extern "C" {
#endif

deList *
newList(void)
{   deList *ptr = malloc(sizeof(deList));
    if (ptr == NULL) return NULL;
    memset(ptr, 0, sizeof(deList));
    deListNode *sentinel = malloc(sizeof(deListNode));
    sentinel = newListNodeSentinel();
    ptr->sentinel = sentinel;
    ptr->size = 0;
    return ptr;
}

void
freeList(deList *list)
{   if (list == NULL) return;
    deListNode *sentinel = getListSentinel(list);
    deListNode *node = getListHead(list);
    while (node != sentinel)
    {   deListNode *next_node = getListNodeNext(node);
        free(node);
        node = next_node;
    }
    free(sentinel);
    free(list);
}

int
appendList(deList *ptr, int value)
{   deListNode *new_node;
    new_node = newListNode(value);
    new_node->next = ptr->sentinel;
    new_node->prev = ptr->sentinel->prev;
    ptr->sentinel->prev->next = new_node;
    ptr->sentinel->prev = new_node;
    ptr->size += 1;
    return value;
}

void
deleteList(deList *lst, deListNode *n)
{   if (n == NULL || lst == NULL) return;
    n->prev->next = n->next;
    n->next->prev = n->prev;
    freeListNode(n);
    lst->size -= 1;
}

int
prependList(deList *ptr, int value)
{   deListNode *new_node;
    new_node = newListNode(value);
    new_node->prev = ptr->sentinel;
    new_node->next = ptr->sentinel->next;
    ptr->sentinel->next->prev = new_node;
    ptr->sentinel->next = new_node;
    ptr->size += 1;
    return value;
}

int
searchList(deList *ptr, int value)
{   if (0 < ptr->size)
    {   deListNode *x = ptr->sentinel->next;
        while (x != ptr->sentinel)
        {   if (x->key == value) return value;
            x = x->next;
        }
    }
    return -1;
}

void
graphList(deList *list, FILE *fp)
{   fprintf(fp, "digraph deList {\n");
    fprintf(fp, "    node [fontname=\"Arial\"];\n");
    deListNode *sentinel = getListSentinel(list);
    deListNode *node = getListHead(list);
    while (node != sentinel)
    {   int key = getListNodeKey(node);
        int next_key;
        int prev_key;
        if (node == getListHead(list)) {
            prev_key = getListNodeKey(getListTail(list));
            next_key = getListNodeKey(getListNodeNext(node));
        } else if (node == getListTail(list)) {
            prev_key = getListNodeKey(getListNodePrev(node));
            next_key = getListNodeKey(getListHead(list));
        } else {
            prev_key = getListNodeKey(getListNodePrev(node));
            next_key = getListNodeKey(getListNodeNext(node));
        }
        fprintf(fp, "    node [style=filled,fillcolor=white];\n");
        fprintf(fp, "    %d -> %d;\n", key, next_key);
        fprintf(fp, "    %d -> %d;\n", key, prev_key);
        node = getListNodeNext(node);
    }
    fprintf(fp, "}");
    fclose(fp);
}

int
getListSize(deList *ptr)
{   return ptr->size;
}

deListNode *
getListSentinel(deList *ptr)
{   return ptr->sentinel;
}

deListNode *
getListHead(deList *ptr)
{   return ptr->sentinel->next;
}

deListNode *
getListTail(deList *ptr)
{   return ptr->sentinel->prev;
}

#ifdef __cplusplus
}
#endif
