// 2024.11.11

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(-1);
        ListNode* current = dummy;
        ListNode *curr1 = list1, *curr2 = list2;

        while (curr1 != nullptr && curr2 != nullptr) {
            if (curr1->val <= curr2->val) {
                current->next = curr1;
                curr1 = curr1->next;
            } else {
                current->next = curr2;
                curr2 = curr2 ->next;
            }
            current = current->next;
        }

        current->next = (curr1 != nullptr) ? curr1 : curr2;

        ListNode* merged = dummy->next;
        delete dummy;

        return merged;
    }
};