// 2023.02.08

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2) {
    struct ListNode *tmp, *tail, *head;
    head = tail = NULL;

    int carry = 0, sum;
    while (l1 || l2 || carry) {
        tmp = (struct ListNode *)malloc(sizeof(struct ListNode));
        sum = (l1 == NULL ? 0 : l1->val) + (l2 == NULL ? 0 : l2->val) + carry;
        carry = sum / 10;
        sum %= 10;
        tmp->val = sum;
        tmp->next = NULL;
        if (head == NULL)
            head = tmp;
        else
            tail->next = tmp;
        tail = tmp;
        l1 = l1 == NULL ? NULL : l1->next;
        l2 = l2 == NULL ? NULL : l2->next;
    }
    return head;
}

