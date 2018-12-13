#!/bin/bash
int find(char* a, int n, char key){
    if(a == null || n <=0){
        return -1;
    }
    int i = 0;
    while(i < n){
       if (a[i] == key){
           return i;
       }
       ++i;
    }
    return -1;
}

int find(char* a, int n, char key){
    if(a == null || n <= 0){
        return -1;
    }
    if (a[n-1] == key){
        return n-1;
    }
    char tmp = a[n-1];
    a[n-1] = key;
    int i = 0;
    while (a[i] != key){
         ++i;
    }
    if (i == n-1){
        return -1;
    }
    else {
        return i;
    }   
}

