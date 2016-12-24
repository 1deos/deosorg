/* Copyright (c) 2013-2016 Andrew T. DeSantis */

#include "atdlib.h"

/* Declarations */
static int testDeleteTree(void);
static int testDeleteTreeTwo(void);
static int testDeleteTreeThree(void);
static int testDeleteTreeFour(void);
static int testGraphTree(void);
static int testNewTreeNode(void);
static int testNewTree(void);
static int testInsertTree(void);
static int testInsertTreeTwo(void);

/* Main Function */
int main(int argc, char *argv[])
{
    int test = 0;
    test += testNewTreeNode();
    test += testNewTree();
    test += testInsertTree();
    test += testInsertTreeTwo();
    test += testGraphTree();
    test += testDeleteTree();
    test += testDeleteTreeTwo();
    test += testDeleteTreeThree();
    test += testDeleteTreeFour();
    printf("%d\n", test);
    return EXIT_SUCCESS;
}

/* Helper Functions */
static int testDeleteTree(void)
{
    deTree *tree = newTree();
    insertTree(tree, 21);
    insertTree(tree, 20);
    insertTree(tree, 23);
    insertTree(tree, 22);
    insertTree(tree, 100);
    insertTree(tree, 10);
    insertTree(tree, 200);
    insertTree(tree, 12);
    insertTree(tree, 5);
    insertTree(tree, 15);
    insertTree(tree, 201);
    deTreeNode *node = insertTree(tree, 188);
    deleteTree(tree, node);
    FILE *fp = fopen("./tst/deTree.dot", "w+");
    graphTree(tree, fp);
    freeTree(tree);
    fclose(fp);
    return 0;
}

static int testDeleteTreeTwo(void)
{
    deTree *tree = newTree();
    insertTree(tree, 21);
    deTreeNode *node = insertTree(tree, 20);
    insertTree(tree, 23);
    insertTree(tree, 22);
    insertTree(tree, 100);
    insertTree(tree, 10);
    insertTree(tree, 200);
    insertTree(tree, 12);
    insertTree(tree, 5);
    insertTree(tree, 15);
    insertTree(tree, 201);
    insertTree(tree, 188);
    deleteTree(tree, node);
    FILE *fp = fopen("./tst/deTree.dot", "w+");
    graphTree(tree, fp);
    freeTree(tree);
    fclose(fp);
    return 0;
}

static int testDeleteTreeThree(void)
{
    deTree *tree = newTree();
    insertTree(tree, 21);
    insertTree(tree, 20);
    deTreeNode *node = insertTree(tree, 23);
    insertTree(tree, 22);
    insertTree(tree, 100);
    insertTree(tree, 10);
    insertTree(tree, 200);
    insertTree(tree, 12);
    insertTree(tree, 5);
    insertTree(tree, 15);
    insertTree(tree, 201);
    insertTree(tree, 188);
    deleteTree(tree, node);
    FILE *fp = fopen("./tst/deTree.dot", "w+");
    graphTree(tree, fp);
    freeTree(tree);
    fclose(fp);
    return 0;
}

static int testDeleteTreeFour(void)
{
    deTree *tree = newTree();
    deTreeNode *node = insertTree(tree, 21);
    insertTree(tree, 20);
    insertTree(tree, 23);
    insertTree(tree, 22);
    insertTree(tree, 100);
    insertTree(tree, 10);
    insertTree(tree, 200);
    insertTree(tree, 12);
    insertTree(tree, 5);
    insertTree(tree, 15);
    insertTree(tree, 201);
    insertTree(tree, 188);
    deleteTree(tree, node);
    FILE *fp = fopen("./tst/deTree.dot", "w+");
    graphTree(tree, fp);
    freeTree(tree);
    fclose(fp);
    return 0;
}

static int testGraphTree(void)
{
    deTree *tree = newTree();
    insertTree(tree, 21);
    insertTree(tree, 20);
    insertTree(tree, 23);
    insertTree(tree, 22);
    insertTree(tree, 100);
    insertTree(tree, 10);
    insertTree(tree, 200);
    insertTree(tree, 12);
    insertTree(tree, 5);
    insertTree(tree, 15);
    insertTree(tree, 201);
    insertTree(tree, 188);
    FILE *fp = fopen("./tst/deTree.dot", "w+");
    graphTree(tree, fp);
    freeTree(tree);
    fclose(fp);
    return 0;
}

static int testNewTreeNode(void)
{
    deTreeNode *node = newTreeNode(21);
    int key = getTreeNodeKey(node);
    freeTreeNode(node);
    if (key == 21) return 0;
    return 1;
}

static int testNewTree(void)
{
    deTree *tree = newTree();
    int size = getTreeSize(tree);
    freeTree(tree);
    if (size == 0) return 0;
    return 1;
}

static int testInsertTree(void)
{
    deTree *tree = newTree();
    insertTree(tree, 21);
    deTreeNode *root = getTreeRoot(tree);
    int key = getTreeNodeKey(root);
    int size = getTreeSize(tree);
    freeTree(tree);
    if (key == 21 && size == 1) return 0;
    return 1;
}

static int testInsertTreeTwo(void)
{
    deTree *tree = newTree();
    insertTree(tree, 21);
    insertTree(tree, 22);
    insertTree(tree, 20);
    int size = getTreeSize(tree);
    freeTree(tree);
    if (size == 3) return 0;
    return 1;
}
