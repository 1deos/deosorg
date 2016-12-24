/* Copyright (c) 2013-2016 Andrew T. DeSantis */

#include "atdlib.h"

void testFreeList(void)
{
    deList *ptr;
    ptr = newList();

    int i;
    for (i = 1; i < 1000; ++i)
    {
        appendList(ptr, i);
    }

    freeList(ptr);
}

void testGraphList(void)
{
    deList *list;
    list = newList();

    int i;
    for (i = 1; i < 10; ++i)
    {
        appendList(list, i);
    }

    FILE *fp = fopen("./test/deList.dot", "w+");
    graphList(list, fp);
    freeList(list);
}

int testDeleteList(void)
{
    deList *ptr;
    ptr = newList();

    int i;
    for (i = 1; i < 1000; ++i)
    {
        appendList(ptr, i);
    }

    int j;
    for (j = 1; j < 1000; ++j)
    {
        deListNode *node;
        node = getListHead(ptr);
        deleteList(ptr, node);
    }

    printf("%d\n", getListSize(ptr));

    freeList(ptr);
    return 0;
}

int testAppendList(void)
{
    deList *ptr;
    ptr = newList();

    int size;
    size = getListSize(ptr);
    if (size != 0) return 1;

    int i;
    for (i = 1; i < 1001; ++i)
    {
        appendList(ptr, i);
    }

    size = getListSize(ptr);
    if (size != 1000) return 1;

    freeList(ptr);
    return 0;
}

int testPrependList(void)
{
    deList *ptr;
    ptr = newList();

    int size;
    size = getListSize(ptr);
    if (size != 0) return 1;

    int i;
    for (i = 1; i < 1001; ++i)
    {
        prependList(ptr, i);
    }

    size = getListSize(ptr);
    if (size != 1000) return 1;

    freeList(ptr);
    return 0;
}

int testSearchList(void)
{
    deList *ptr;
    ptr = newList();

    int i;
    for (i = 1; i < 1000; ++i)
    {
        appendList(ptr, i);
    }

    int j;
    for (j = 1; j < 1000; ++j)
    {
        if (searchList(ptr, j) == -1)
        {
            printf("%d\n", j);
            return 1;
        }
    }

    freeList(ptr);
    return 0;
}

int main(int argc, char *argv[])
{
    int test = 0;
    test += testAppendList();
    test += testSearchList();
    test += testPrependList();
    test += testDeleteList();
    printf("%d\n", test);
    return 0;
}
