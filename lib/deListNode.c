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

#include "deListNode.h"

#ifdef __cplusplus
extern "C" {
#endif

deListNode *
newListNode(int key)
{   /* create deListNode pointer */
    deListNode *ptr = malloc(sizeof(deListNode));
    /* confirm pointer creation */
    if (ptr == NULL) return NULL;
    /* fill memory with a constant byte */
    memset(ptr, 0, sizeof(deListNode));
    /* set member values */
    setListNodeKey(ptr, key);
    ptr->next = NULL;
    ptr->prev = NULL;
    return ptr;
}

deListNode *
newListNodeSentinel(void)
{   /* create deListNode pointer */
    deListNode *ptr = malloc(sizeof(deListNode));
    /* confirm pointer creation */
    if (ptr == NULL) return NULL;
    /* fill memory with a constant byte */
    memset(ptr, 0, sizeof(deListNode));
    /* set member values */
    ptr->next = ptr;
    ptr->prev = ptr;
    return ptr;
}

void
freeListNode(deListNode *ptr)
{   if (ptr == NULL) return;
    free(ptr);
}

int
getListNodeKey(deListNode *ptr)
{   return ptr->key;
}

deListNode *
getListNodeNext(deListNode *ptr)
{   return ptr->next;
}

deListNode *
getListNodePrev(deListNode *ptr)
{   return ptr->prev;
}

int
setListNodeKey(deListNode *ptr, int key)
{   int old_key = ptr->key;
    ptr->key = key;
    return old_key;
}

#ifdef __cplusplus
}
#endif
