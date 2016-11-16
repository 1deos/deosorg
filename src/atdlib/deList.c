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
