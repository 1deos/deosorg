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
