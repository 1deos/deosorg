/* BSD 2-Clause License

Copyright (c) 2013-2016 Andrew T. DeSantis. All rights reserved.
Copyright (c) 2016 DeSantis Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#ifndef __DETREE__
#define __DETREE__

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __ATDLIB__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#endif

#include "deTreeNode.h"

typedef struct deTreeObject
{   int size;
	deTreeNode *NIL;
	deTreeNode *root;
} deTree;

extern deTree *newTree(void);
extern void freeTree(deTree *self);
extern void deleteTree(deTree *self, deTreeNode *node);
extern void graphTree(deTree *self, FILE *fp);
extern deTreeNode *insertTree(deTree *self, int value);
extern deTreeNode *maximumTree(deTree *self);
extern deTreeNode *minimumTree(deTree *self);
extern deTreeNode *minimumSubTree(deTree *self, deTreeNode *node);
extern deTreeNode *getTreeNil(deTree *self);
extern deTreeNode *getTreeRoot(deTree *self);
extern int getTreeSize(deTree *self);
extern void setTreeRoot(deTree *self, deTreeNode *node);

#ifdef __cplusplus
}
#endif

#endif /* __DETREE__ */
