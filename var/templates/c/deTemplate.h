/*
* Copyright (c) 2013-2016 Andrew DeSantis
* Copyright (c) 2016 DeSantis Inc.
*/

#ifndef __DE<T>__
#define __DE<T>__

#ifdef __cplusplus
extern "C" {
#endif

/* STD Library */
#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

/* Definition */
typedef struct de<T>Object
{   int type;
} de<T>;

/* Constructors */
extern de<T> *new<T>(int type);

/* Destructor */
extern int free<T>(de<T> *self);

/* Getters */
extern int get<T>Type(de<T> *self);

/* Setters */
extern int set<T>Type(de<T> *self, int type);

#ifdef __cplusplus
}
#endif

#endif /* __DE<T>__ */
