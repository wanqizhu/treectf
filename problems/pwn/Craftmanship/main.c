#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>



void craft() {
    char buff[100];
    printf("Show me your crafting skills: ");
    fgets(buff, 200, stdin);
    printf("You have much to learn grasshopper.\n");
}

int main() {
    craft();
    return 0;
}
