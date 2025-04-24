#include "Questions.h"
#include <stdio.h>
#include<string.h>
#include<stdlib.h>
#include "Utils.h"
#define CRUSH_LENGTH 50
#define YOUR_LENGTH 50

void question_1(){
FILE* ptr;
ptr = fopen("match.txt","w");
if(ptr == NULL){
    perror("does not exist");
    return;
}
    int score = 0;
    char CRUSH[CRUSH_LENGTH],YOU[YOUR_LENGTH]; //size declared in the Headers
printf("Enter your crush name: ");
fgets(CRUSH,CRUSH_LENGTH,stdin);
fprintf(ptr,"\tCrush name: %s",CRUSH);
clearInputbuffer(); //To consume the newline character
printf("\nEnter your name: ");
fgets(YOU,YOUR_LENGTH,stdin);         //To keep track of the names using a storage known as FILE
fprintf(ptr,"\tYour name: %s",YOU);

if(strcmp(CRUSH,YOU) == 0){
    printf("Name match good start :)");
}else{

}
fclose(ptr);


}
