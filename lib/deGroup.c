/* ΔOS: Decentralized Operating System

Copyright (c) 2013-2017 Andrew DeSantis <atd@gmx.it>
Copyright (c) 2016-2017 DeSantis Inc. <inc@gmx.it>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

This file incorporates work covered by the BSD 2-Clause License,
as well as the following copyright, and permission notice:
---
ΔOS may be used and distributed under the terms of the GPLv3,
which are available at: <http://www.gnu.org/licenses/gpl-3.0.html>

If you would like to embed ΔOS within a commercial application or
redistribute it in a modified binary form, contact DeSantis Inc.
*/

#include "deGroup.h"

#ifdef __cplusplus
extern "C" {
#endif

deGroup *
newGroup(int type)
{   deGroup *self = (deGroup *) malloc(sizeof(deGroup));
    if (self == NULL) return NULL;
    memset(self, 0, sizeof(deGroup));
    if (setGroupType(self, 1) < 1)
    {   freeGroup(self);
        self = NULL;
    }
    return self;
}

int
freeGroup(deGroup *self)
{   if (NULL == self) return -1;
    free(self);
    return 0;
}

int
getGroupType(deGroup *self)
{   if (NULL == self) return -1;
    return self->type;
}

int
setGroupType(deGroup *self, int type)
{   if (1 > type) return 0; /* bad type */
    self->type = type; /* assign type */
    if (self->type == type) /* if type set */
        return self->type; /* return type */
    return -1; /* assign error */
}

#ifdef __cplusplus
}
#endif
