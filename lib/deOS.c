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

  Copyright (c) 2013-2017 Andrew DeSantis. All rights reserved.
  Copyright (c) 2016-2017 DeSantis Inc. All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:

  * Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
  COPYRIGHT HOLDER COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
  OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
  BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
  OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

ΔOS may be used and distributed under the terms of the GPLv3,
which are available at: <http://www.gnu.org/licenses/gpl-3.0.html>

If you would like to embed ΔOS within a commercial application or
redistribute it in a modified binary form, contact DeSantis Inc.
*/

#include "deOS.h"

#ifdef __cplusplus
extern "C" {
#endif

static void _initObject(deOS *os);

deOS *
newOS(void)
{   deOS *os = (deOS *) malloc(sizeof(deOS));
    if (os == NULL) return NULL;
    memset(os, 0, sizeof(deOS));
    _initObject(os);
    os->shell = NULL;
    if (getOSType(os) != TYPE_OS)
    {   freeOS(os);
        return NULL;
    }
    return os;
}

int
freeOS(deOS *os)
{   if (NULL == os) return -1;
    if (NULL != os->self) freeObject(os->self);
    if (NULL != os->shell) freeShell(os->shell);
    free(os);
    return 0;
}

int
getOSType(deOS *os)
{   if (NULL == os) return -1;
    if (NULL == os->self) return -2;
    int type = getObjectType(os->self);
    return type;
}

int
setOSShell(deOS *os, deShell *shell)
{   if (NULL == os) return -1;
    else if (NULL == shell) return -2;
    os->shell = shell;
    return 0;
}

static void
_initObject(deOS *os)
{   deObject *obj = newObject(TYPE_OS);
    os->self = obj;
}

#ifdef __cplusplus
}
#endif
