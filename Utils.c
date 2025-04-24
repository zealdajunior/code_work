#include<ctype.h>
#include<stdio.h>
#include<unistd.h>
#include "Utils.h"
void clearInputbuffer(){
int c;
while((c = getchar()) != '\n' && c!=EOF);
}

void loadingBar(int choice){
int barlength = 20;
int progress = 0;
printf("Loading...\n");
while(progress < barlength){
    printf("\r[");
    for(int i = 0; i < progress; i++){
        printf("/");
    }
    for(int i = 0; i < barlength - progress; i++){
        printf(" ");
    }
    printf("] %d%%",(progress * 100) / barlength);
    usleep(500000); //simulate loading time (500ms)
    progress ++;
}
printf("\n");
}

