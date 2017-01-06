#ifndef __DEBACKUP__
#define __DEBACKUP__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

typedef struct deBackupObject
{   int id;
} deBackup;

extern deBackup *newBackup(int id);

#ifdef __cplusplus
}
#endif

#endif /* __DEBACKUP__ */
