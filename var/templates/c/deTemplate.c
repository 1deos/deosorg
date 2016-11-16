/*
* Copyright (c) 2013-2016 Andrew DeSantis
* Copyright (c) 2016 DeSantis Inc.
*/

/* ATD Library */
#include "de<T>.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Constructors */
de<T> *new<T>(int type)
{   de<T> *self = (de<T> *) malloc(sizeof(de<T>));
    if (self == NULL) return NULL;
    memset(self, 0, sizeof(de<T>));
    if (set<T>Type(self, 1) < 1)
    {
        free<T>(self);
        self = NULL;
    }
    return self;
}

/* Destructor */
int free<T>(de<T> *self)
{   if (NULL == self) return -1;
    free(self);
    return 0;
}

/* Getters */
int get<T>Type(de<T> *self)
{   if (NULL == self) return -1;
    return self->type;
}

/* Setters */
int set<T>Type(de<T> *self, int type)
{   if (1 > type) return 0; /* bad type */
    self->type = type; /* assign type */
    if (self->type == type) /* if type set */
        return self->type; /* return type */
    return -1; /* assign error */
}

#ifdef __cplusplus
}
#endif
