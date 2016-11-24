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

#include "deArray.h"

#ifdef __cplusplus
extern "C" {
#endif

#define _correctArrayIndex(T,x,s,a) _correctArrayIndex_##T(x,s,a)
#define _growArray(T,x) _growArray_##T(x)
#define deArrayPolymorphismC(T)                                               \
                                                                              \
static void _correctArrayIndex_##T(deArray_##T *self, char *side, char *act); \
static void _growArray_##T(deArray_##T *self);                                \
                                                                              \
deArray_##T *newArray_##T(void)                                               \
{                                                                             \
    deArray_##T *self = (deArray_##T *) malloc(sizeof(deArray_##T));          \
    self->factor = FACTOR;                                                    \
    self->capacity = CAPACITY;                                                \
    self->store = (T *) malloc(self->capacity * sizeof(T));                   \
    self->head = self->tail = self->size = 0;                                 \
    return self;                                                              \
}                                                                             \
                                                                              \
void freeArray_##T(deArray_##T *self)                                         \
{                                                                             \
    if (self == NULL) return;                                                 \
    free(self->store);                                                        \
    free(self);                                                               \
}                                                                             \
                                                                              \
void appendArray_##T(deArray_##T *self, int value)                            \
{                                                                             \
    if (self->size == 0)                                                      \
        prependArray_##T(self, value);                                        \
    else                                                                      \
    {                                                                         \
        if (getArraySize_##T(self) == getArrayCapacity_##T(self))             \
            _growArray_##T(self);                                             \
        else                                                                  \
            _correctArrayIndex_##T(self, "tail", "increment");                \
        self->store[getArrayTail_##T(self)] = value;                          \
        self->size++;                                                         \
    }                                                                         \
}                                                                             \
                                                                              \
void prependArray_##T(deArray_##T *self, int value)                           \
{                                                                             \
    if (getArraySize_##T(self) == 0)                                          \
    {                                                                         \
        self->store[getArrayTail_##T(self)] = value;                          \
        self->size++;                                                         \
    }                                                                         \
    else                                                                      \
    {                                                                         \
        if (getArraySize_##T(self) == getArrayCapacity_##T(self))             \
            _growArray_##T(self);                                             \
        _correctArrayIndex_##T(self, "head", "decrement");                    \
        self->store[getArrayHead_##T(self)] = value;                          \
        self->size++;                                                         \
    }                                                                         \
}                                                                             \
                                                                              \
double getArrayFactor_##T(deArray_##T *self)                                  \
{                                                                             \
    return self->factor;                                                      \
}                                                                             \
                                                                              \
int getArrayCapacity_##T(deArray_##T *self)                                   \
{                                                                             \
    return self->capacity;                                                    \
}                                                                             \
                                                                              \
int getArrayHead_##T(deArray_##T *self)                                       \
{                                                                             \
    return self->head;                                                        \
}                                                                             \
                                                                              \
int getArrayTail_##T(deArray_##T *self)                                       \
{                                                                             \
    return self->tail;                                                        \
}                                                                             \
                                                                              \
int getArraySize_##T(deArray_##T *self)                                       \
{                                                                             \
    return self->size;                                                        \
}                                                                             \
                                                                              \
static void _correctArrayIndex_##T(deArray_##T *self, char *side, char *act)  \
{                                                                             \
    if (strcmp(side,"tail") == 0)                                             \
    {                                                                         \
        if (strcmp(act,"increment") == 0)                                     \
            self->tail = (++self->tail) % getArrayCapacity_##T(self);         \
    }                                                                         \
    else                                                                      \
    {                                                                         \
        if (strcmp(act,"decrement") == 0)                                     \
        {                                                                     \
            if (self->head - 1 < 0)                                           \
                self->head = ((--self->head) % getArrayCapacity_##T(self))    \
                                             + getArrayCapacity_##T(self);    \
            else                                                              \
                self->head = ((--self->head) % getArrayCapacity_##T(self));   \
        }                                                                     \
    }                                                                         \
}                                                                             \
                                                                              \
static void _growArray_##T(deArray_##T *self)                                 \
{                                                                             \
    self->head = 0;                                                           \
    self->tail = getArraySize_##T(self);                                      \
    self->capacity = getArrayFactor_##T(self) * getArrayCapacity_##T(self);   \
    self->store = (T *) realloc(self->store,                                  \
                                getArrayCapacity_##T(self) * sizeof(T));      \
}

#define X(T) deArrayPolymorphismC(T);
X(char)                                                                       \
X(double)                                                                     \
X(int)
#undef X
#undef deArrayPolymorphismC

#ifdef __cplusplus
}
#endif
