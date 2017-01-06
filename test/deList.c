#include "atdlib.h"

const int ERROR = 1;

static void
testFreeList(void)
{   deList *ptr = newList();
    int i;
    for (i=1; i<1000; ++i)
    {   appendList(ptr,i);
        /* printf("%d\n",i);
        */
    }
    freeList(ptr);
}

static int
testDeleteList(void)
{   deList *ptr = newList();
    int i;
    for (i=1; i<1000; ++i) appendList(ptr,i);
    int j;
    for (j=1; j<1000; ++j)
    {   deListNode *node = getListHead(ptr);
        deleteList(ptr,node);
    }
    printf("%d\n", getListSize(ptr));
    freeList(ptr);
    return(0);
}

static void
testGraphList(void)
{   deList *list = newList();
    int i;
    for (i=1; i<10; ++i) appendList(list,i);
    FILE*fp=fopen("docs/atdlib/deList.dot","w+");
    graphList(list,fp);
    freeList(list);
}

static int
testAppendList(void)
{   deList *ptr = newList();
    int res = 0, size = getListSize(ptr);
    if (size != 0) res = ERROR;
    else
    {   int i;
        for (i=1; i<1001; ++i) appendList(ptr,i);
        size = getListSize(ptr);
        if (size != 1000) res = ERROR;
    }
    freeList(ptr);
    return res;
}

static
int(testPrependList(void))
    {deList*ptr=newList();
    int(res)=0,(size)=getListSize(ptr);
    if(size!=0){(res)=ERROR;
    }else{
        int(i);for(i=1;i<1001;++i)
            {prependList(ptr,i);
        }(size)=getListSize(ptr);
        if(size!=1000){(res)=ERROR;
    }}freeList(ptr);
    return(res);}

static
int(testSearchList(void))
    {deList*ptr=newList();
    int(i);for(i=1;i<1000;++i)
        {appendList(ptr,i);
    }int(j);for(j=1;j<1000;++j)
        {if(searchList(ptr,j)==(-1))
            {printf("%d\n",j);
            return(ERROR);
            }}freeList(ptr);
    return(0);}

int(main(int(argc),char*(argv[])))
    {int(test)=0;
    testFreeList();
    testGraphList();
    test+=testAppendList();
    test+=testSearchList();
    test+=testPrependList();
    test+=testDeleteList();
    printf("%d\n",test);
    return(EXIT_SUCCESS);}
