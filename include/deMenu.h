#ifndef __DEMENU__
#define __DEMENU__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deMenuObject
{   int id;
} deMenu;

extern deMenu *newMenu(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEMENU__ */
