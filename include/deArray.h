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

#ifndef __DEARRAY__
#define __DEARRAY__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

#define CAPACITY 4
#define FACTOR 2

#define deArray(T) deArray_##T
#define newArray(T) newArray_##T()
#define freeArray(T,x) freeArray_##T(x)
#define appendArray(T,x,v) appendArray_##T(x,v)
#define prependArray(T,x,v) prependArray_##T(x,v)
#define getArrayFactor(T,x) getArrayFactor_##T(x)
#define getArrayCapacity(T,x) getArrayCapacity_##T(x)
#define getArrayHead(T,x) getArrayHead_##T(x)
#define getArrayTail(T,x) getArrayTail_##T(x)
#define getArraySize(T,x) getArraySize_##T(x)
#define deArrayPolymorphismH(T)                                               \
                                                                              \
typedef struct deArrayObject_##T                                              \
{   T *store;                                                                 \
    int size;                                                                 \
    int head;                                                                 \
    int tail;                                                                 \
    int capacity;                                                             \
    double factor;                                                            \
} deArray_##T;                                                                \
                                                                              \
extern deArray_##T *newArray_##T(void);                                       \
extern void freeArray_##T(deArray_##T *self);                                 \
extern void appendArray_##T(deArray_##T *self, int value);                    \
extern void prependArray_##T(deArray_##T *self, int value);                   \
extern int getArrayCapacity_##T(deArray_##T *self);                           \
extern double getArrayFactor_##T(deArray_##T *self);                          \
extern int getArrayHead_##T(deArray_##T *self);                               \
extern int getArrayTail_##T(deArray_##T *self);                               \
extern int getArraySize_##T(deArray_##T *self);

#define X(T) deArrayPolymorphismH(T);
X(char)                                                                       \
X(double)                                                                     \
X(int)
#undef X
#undef deArrayPolymorphismH

#ifdef __cplusplus
}
#endif

#endif /* __DEARRAY__ */
