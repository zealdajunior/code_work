#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>
#include<unistd.h>
#include "Questions.h"
#include "Utils.h"

void Handle_menu(){
    int choice;
printf("\t\t\t\t-----------------Welcome to Hu-Match Game!-------------------\n");
printf("1 -> Check match with a Lover\n");
printf("2 -> Check match with a Friend\n");
printf("3 -> No what would happen in your future\n");
printf("4 -> Exit()_game :(\n");
printf("Choose an option : \n");
while(scanf("%d",&choice) != 1){
    printf("Enter a number and not a letter: ");

    //clear the buffer input
    int c;
    while((c = getchar()) != '\n' &&  c != EOF);
}
 if(choice < 1){
        printf("Cannot take negative numbers\n");
    }

loadingBar(choice);

switch(choice){
case 1:
    // clearing the terminal after each choice made
    #ifdef _WIN32
    system("cls");
    #else
    system("clear");
    #endif // _WIN32
    question_1();
    break;
case 2:
    break;
case 3:
    break;
case 4:
    break;
default:
    exit(EXIT_FAILURE);
}
}
// CH represents choice
int main(){
Handle_menu();
return 0;
}
