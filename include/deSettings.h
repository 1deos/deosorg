#ifndef __DESETTINGS__
#define __DESETTINGS__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deSettingsObject
{   int id;
} deSettings;

extern deSettings *newSettings(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DESETTINGS__ */
