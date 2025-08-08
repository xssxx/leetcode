/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if (!head || !head->next) 
        return head;

    struct ListNode dummy;
    dummy.next = head;

    struct ListNode* prev = &dummy;

    while (prev->next && prev->next->next) {
        struct ListNode* low = prev->next; 
        struct ListNode* hi = low->next; 
        // swap
        low->next = hi->next;
        hi->next = low;
        prev->next = hi;
        // move to next pair
        prev = low;
    }

    return dummy.next;
}