#include <stdio.h>

#define MAXSIZE 100
#define ElemType int

typedef struct {
    ElemType data[MAXSIZE]; // Static array to store elements
    int length; // Current length of the list
} SqList;

void InitList(SqList &L) { // Initialize an empty list
    L.length = 0;
}

bool ListEmpty(SqList L) { // Check if the list is empty
    return L.length == 0;
}

bool ListFull(SqList L) { // Check if the list is full
    return L.length == MAXSIZE;
}



int main() {
    printf("Welcome to Static Sequence List World!\n");
    SqList L;
    InitList(L);
    return 0;
}