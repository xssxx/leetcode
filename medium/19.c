// 2023.03.23

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode Node;

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    if (head == NULL) {
        return NULL;
    }

    Node *temp = head;
    int len = 0;
    while (temp != NULL) {
        temp = temp->next;
        len++;
    }

    if (n >= len) {
        Node *del = head;
        head = head->next;
        free(del);
        return head;
    }

    temp = head;
    Node *prev = NULL;
    for (int i = 0; i < len - n; i++) {
        prev = temp;
        temp = temp->next;
    }

    Node *del = temp;
    if (temp == head) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }
    free(del);

    return head;
}