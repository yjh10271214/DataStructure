#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>   // For sleep() function

// #define MAXSIZE 100
#define INITIAL_SIZE 10
#define INCREASE_SIZE 10

typedef int ElemType;

typedef struct {
    ElemType *data; // Pointer to dynamically allocated array
    int length; // Current length of the list
    int capacity; // Maximum capacity of the list
} SqList;

enum MenuOptions {
    EXIT = 0,
    ADD_ELEM_TO_END,
    DELETE_ELEM_TO_END,
    DELETE_ELEM_BY_VALUE,
    DELETE_ELEM_BY_POS,
    INSERT_ELEM,
    CHANGE_ELEM,
    GET_ELEM,
    PRINT_LIST
};

void InitList(SqList &L) { // Initialize an empty list
    L.data = (ElemType *)malloc(sizeof(ElemType) * INITIAL_SIZE);
    if (L.data == NULL) {
        printf("Memory allocation failed!!!\n");
        exit(-1);
    }

    L.length = 0;
    L.capacity = INITIAL_SIZE;
}

void ListIncreaseCapacity(SqList &L) {
    ElemType *newData = (ElemType *)malloc(sizeof(ElemType) * (L.capacity + INCREASE_SIZE));
    if (newData == NULL) {
        printf("Memory allocation failed while increasing capacity!!!\n");
        exit(-1);
    }
    
    //copy old data to new data
    for (int i = 0; i < L.length; i++) {
        newData[i] = L.data[i];
    }

    free(L.data); //free old data
    L.data = newData;
    L.capacity += INCREASE_SIZE;

    printf("\t\t\tList capacity increased to %d successfully!!!!\n", L.capacity);
}

bool ListIsEmpty(SqList L) { // Check if the list is empty
    return L.length == 0;
}

bool ListIsFull(SqList L) { // Check if the list is full
    return L.length == L.capacity;
}

bool ListAddElemToEnd(SqList &L, ElemType elem) { // Add an element to the end of the list
    if (ListIsFull(L)) {
        printf("add warning: List is full, do you have increasing capacity!!!\n");
        printf("please input y/n: ");
        char choice;
        scanf(" %c", &choice);
        if (choice == 'y' || choice == 'Y') {
            ListIncreaseCapacity(L);
        }
        
        return false;
    }

    L.data[L.length] = elem; // Add elem at the end
    L.length++;
    printf("Element %d added to the end of the list, current length: %d\n", elem, L.length);
    return true; // Addition successful
}

bool ListDeleteElemToEnd(SqList &L) { // Delete an element from the end of the list
    if (ListIsEmpty(L)) {
        printf("delete error: List is empty, cannot delete element!!!\n");
        return false;
    }

    ElemType deletedElem = L.data[L.length - 1]; // Get the last element
    L.length--; // Decrease length
    printf("Element %d deleted from the end of the list, current length: %d\n", deletedElem, L.length);
    return true; // Deletion successful
}

bool ListDeleteElemByValue(SqList &L, ElemType elem) { //Delete an element from the list by value
    if (ListIsEmpty(L)) {
        printf("delete error: List is empty, cannot delete element!!!\n");
        return false;
    }

    //first: find the position of element
    int count = 0;
    for (int i = 0; i < L.length; i++) {
        if (L.data[i] == elem) {
            count++;
            //second: move elements after i to the left
            for (int j = i + 1; j < L.length; j++) {
                L.data[j - 1] = L.data[j];
            }
            //third: decrease length
            L.length--;
            i--; //adjust index after deletion
        }
    }
    printf("Element %d overall %d numbers deleted from the list, current length: %d\n", elem, count, L.length);
    return true; //Deletion successful
}

bool ListDeleteElemByPos(SqList &L, int pos) { //Delete an element from the list by position
    if (ListIsEmpty(L)) {
        printf("delete error: List is empty, cannot delete element!!!\n");
        return false;
    }
    if (pos < 1 || pos > L.length) {
        printf("delete error: Invalid position to delete element!!!\n");
        return false;
    }

    printf("Element %d at postion %d to be deleted.\n", L.data[pos - 1], pos);
    //first: move elements after pos to the left
    for (int i = pos; i < L.length; i++) {
        L.data[i - 1] = L.data[i];
    }
    //second: decrease length
    L.length--;
    return true; //Deletion successful
}

bool ListInsertElem(SqList &L, int elem, int pos) { //Insert an element into the list
    if (ListIsFull(L)) {
        printf ("insert error: List is full, cannot insert element!!!\n");
        return false;
    }
    if (pos < 1 || pos > L.length + 1) {
        printf("insert error: Invalid position to insert element!!!\n");
        return false;
    }
    //first :move elements after pos to the right
    for (int i = L.length; i > pos; i--) {
        L.data[i] = L.data[i - 1];
    }
    //second: insert elem at pos
    L.data[pos - 1] = elem;
    L.length++;
    return true; //Insertion successful
}

bool ListChageElem(SqList &L, int pos, ElemType elem) { //Change an element in the list
    if (pos < 1 || pos > L.length) {
        printf("change error: Invalid position to change element!!!\n");
        return false;
    }

    //change elem at pos
    printf("Element at position %d changed from %d to %d.\n", pos, L.data[pos - 1], elem);
    L.data[pos - 1] = elem;
    return true; //Change successful
}

bool ListGetElem(SqList &L, int pos, ElemType &elem) { //Get an element from the list
    if (pos < 1 || pos > L.length) {
        printf("get error: Invalid position to get element!!!\n");
        return false;
    }

    //get elem at pos
    elem = L.data[pos - 1];
    return true; //Get sucessful
}

bool ListPrint(SqList L) { //Print the list
    if (ListIsEmpty(L)) {
        printf("print error: List is empty, cannot print elements!!!\n");
        return false;
    }

    printf("List elements: ");
    for (int i = 0; i < L.length; i++) {
        printf("%d ", L.data[i]);
    }
    printf("\n");
    return true; //Print successful
}

void ShowMenu() { // Display menu options
    system("clear");
    printf("****************** Static Sequence List Menu ******************\n");
    printf("\t1. Add Element to End\n");
    printf("\t2. Delete Element from End\n");
    printf("\t3. Delete Element by Value\n");
    printf("\t4. Delete Element by Position\n");
    printf("\t5. Insert Element\n");
    printf("\t6. Change Element\n");
    printf("\t7. Get Element\n");
    printf("\t8. Print List\n");
    printf("\t0. Exit\n");
    printf("***************************************************************\n");
}

void Option_1(SqList &L) { // Handle option 1: Add Element to End
    system("clear");
    printf("****************** Add Element to End ******************\n");
    while (true) {
        ElemType elem;
        printf("Enter element to add: ");
        scanf("%d", &elem);
        ListAddElemToEnd(L, elem);

        printf("Do you want to add another element? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_2(SqList &L) { // Handle option 2: Delete Element from End
    system("clear");
    printf("****************** Delete Element from End ******************\n");
    while (true) {
        ListDeleteElemToEnd(L);
        printf("Do you want to delete another element from end? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_3(SqList &L) { // Handle option 3: Delete Element by Value
    system("clear");
    printf("****************** Delete Element by Value ******************\n");
    while (true) {
        ElemType elem;
        printf("Enter element value to delete: ");
        scanf("%d", &elem);
        ListDeleteElemByValue(L, elem);

        printf("Do you want to delete another element by value? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_4(SqList &L) { // Handle option 4: Delete Element by Position
    system("clear");
    printf("****************** Delete Element by Position ******************\n");
    while (true) {
        int pos;
        printf("Enter position to delete element: ");
        scanf("%d", &pos);
        ListDeleteElemByPos(L, pos);

        printf("Do you want to delete another element by position? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_5(SqList &L) { // Handle option 5: Insert Element
    system("clear");
    printf("****************** Insert Element ******************\n");
    while (true) {
        ElemType elem;
        int pos;
        printf("Enter element to insert: ");
        scanf("%d", &elem);
        printf("Enter position to insert element: ");
        scanf("%d", &pos);
        ListInsertElem(L, elem, pos);

        printf("Do you want to insert another element? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_6(SqList &L) { // Handle option 6: Change Element
    system("clear");
    printf("****************** Change Element ******************\n");
    while (true) {
        int pos;
        ElemType elem;
        printf("Enter position to change element: ");
        scanf("%d", &pos);
        printf("Enter new element value: ");
        scanf("%d", &elem);
        ListChageElem(L, pos, elem);

        printf("Do you want to change another element? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_7(SqList &L) { // Handle option 7: Get Element
    system("clear");
    printf("****************** Get Element ******************\n");
    while (true) {
        int pos;
        ElemType elem;
        printf("Enter position to get element: ");
        scanf("%d", &pos);
        if (ListGetElem(L, pos, elem)) {
            printf("Element at position %d is %d\n", pos, elem);
        }

        printf("Do you want to get another element? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

void Option_8(SqList &L) { // Handle option 8: Print List
    system("clear");
    printf("****************** Print List ******************\n");
    while (true) {
        ListPrint(L);

        printf("Do you want to print the list again? (y/n): ");
        char choice;
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }
}

int main() {
    SqList L;
    InitList(L);

    while (true) {
        int opt = -1;
        ShowMenu();
        printf("\tPlease select an option: ");
        scanf("%d", &opt);

        switch (opt) {
            case ADD_ELEM_TO_END: {
                Option_1(L);
                break;
            }
            case DELETE_ELEM_TO_END:
                Option_2(L);
                break;
            case DELETE_ELEM_BY_VALUE: {
                Option_3(L);
                break;
            }
            case DELETE_ELEM_BY_POS: {
                Option_4(L);
                break;
            }
            case INSERT_ELEM: {
                Option_5(L);
                break;
            }
            case CHANGE_ELEM: {
                Option_6(L);
                break;
            }
            case GET_ELEM: {
                Option_7(L);
                break;
            }
            case PRINT_LIST:
                Option_8(L);
                break;
            case EXIT:
                printf("Exiting Static Sequence List. Goodbye!\n");
                return 0;
            default:
                printf("Invalid option! Please try again.\n");
        }
    }
    return 0;
}