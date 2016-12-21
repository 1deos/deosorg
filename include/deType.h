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

#ifndef __DETYPE__
#define __DETYPE__

#ifdef __cplusplus
extern "C" {
#endif

#define ENUM_MACRO(T,I) TYPE_##T = I,
#define TYPE_TABLE \
X(1,  ARRAY_CHAR,   "deArray(char) *this"   ) \
X(2,  ARRAY_DOUBLE, "deArray(double) *this" ) \
X(3,  ARRAY_INT,    "deArray(int) *this"    ) \
X(4,  CONTAINER,    "deContainer(int) *this") \
X(5,  NODE,         "deNode *this"          ) \
X(6,  NONE,         "deObject *this"        ) \
X(7,  LIST,         "deList *this"          ) \
X(8,  LIST_NODE,    "deListNode *this"      ) \
X(9,  OBJECT,       "deObject *this"        ) \
X(10, OS,           "deOS *this"            ) \
X(11, SHELL,        "deShell *this"         ) \
X(12, TREE,         "deTree *this"          ) \
X(13, TREE_NODE,    "deTreeNode *this"      )

enum deType {
#define X(I,T,S) ENUM_MACRO(T,I)
TYPE_TABLE
#undef X
} type;

#undef TYPE_TABLE
#undef ENUM_MACRO

#ifdef __cplusplus
}
#endif

#endif /* __DETYPE__ */
