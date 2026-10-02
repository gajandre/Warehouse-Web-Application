#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Item {
    char name[100];
    int quantity;
    char location[100];
    char description[200];
    struct Item* next;
};

struct Item* head = NULL;

void insert(char* name, int quantity, char* location, char* description) {
    struct Item* newItem = malloc(sizeof(struct Item));
    strcpy(newItem->name, name);
    newItem->quantity = quantity;
    strcpy(newItem->location, location);
    strcpy(newItem->description, description);
    newItem->next = head;
    head = newItem;
}

void sortByQuantity() {
    struct Item *i, *j;
    for (i = head; i; i = i->next) {
        for (j = i->next; j; j = j->next) {
            if (i->quantity > j->quantity) {
                // swap all fields
                int tq = i->quantity; i->quantity = j->quantity; j->quantity = tq;

                char temp[200];
                strcpy(temp, i->name); strcpy(i->name, j->name); strcpy(j->name, temp);
                strcpy(temp, i->location); strcpy(i->location, j->location); strcpy(j->location, temp);
                strcpy(temp, i->description); strcpy(i->description, j->description); strcpy(j->description, temp);
            }
        }
    }
}

void display() {
    struct Item* temp = head;
    while (temp) {
        printf("%s|%d|%s|%s\n", temp->name, temp->quantity, temp->location, temp->description);
        temp = temp->next;
    }
}

int main() {
    FILE* f = fopen("items_input.txt", "r");
    if (!f) return 1;

    char name[100], location[100], description[200];
    int quantity;

    while (fscanf(f, "%[^|]|%d|%[^|]|%[^\n]\n", name, &quantity, location, description) != EOF) {
        insert(name, quantity, location, description);
    }
    fclose(f);

    sortByQuantity();  // or sortByName()

    display();  // prints to stdout
    return 0;
}
