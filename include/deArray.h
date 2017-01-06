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
