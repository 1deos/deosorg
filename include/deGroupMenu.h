#ifndef __DEGROUPMENU__
#define __DEGROUPMENU__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deGroupMenuObject
{   int id;
} deGroupMenu;

extern deGroupMenu *newGroupMenu(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEGROUPMENU__ */
