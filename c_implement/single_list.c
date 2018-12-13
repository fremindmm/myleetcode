#include <stdio.h>
#include <stdbool.h>

struct single_list{
    struct single_list *next;
    int val;
};

struct single_list_head{
    struct single_list *head;
};

bool is_empty(struct single_list_head *head){
    return head->head == NULL;
}

void insert(struct single_list **prev, struct single_list *elem){
    if(!prev)
        return;
    if(*prev)
        elem->next = *prev;  
    *prev = elem;
}

int main()
{
    struct single_list_head head = {NULL};
    struct single_list lists[10];
    struct single_list **prev;
    int idx;
    for (idx = 0; idx < 10; idx++){
        lists[idx].val = idx;
        lists[idx].next = NULL;
    }
    
    insert_head(&head, &lists[6]);

}
