#ifndef __DEPASSWDMENU__
#define __DEPASSWDMENU__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct dePasswdMenuObject
{   int id;
} dePasswdMenu;

extern dePasswdMenu *newPasswdMenu(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEPASSWDMENU__ */
