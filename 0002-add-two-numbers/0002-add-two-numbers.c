#include <stdio.h>
#include <stdlib.h>

// Assuming ListNode is already defined as:
// struct ListNode {
//     int val;
//     struct ListNode* next;
// };
// C code 
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy = {0, NULL}; // Dummy node to simplify result list handling
    struct ListNode* current = &dummy; // Pointer to build the result list
    int carry = 0;

    while (l1 || l2 || carry) {
        int sum = carry; // Start with carry

        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }

        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10; // Update carry for the next iteration
        current->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        current->next->val = sum % 10; // Store the current digit
        current->next->next = NULL;    // Initialize next pointer
        current = current->next;      // Move pointer forward
    }

    return dummy.next; // Return the result list
}

// Helper functions for testing
struct ListNode* createLinkedList(int* values, int size) {
    struct ListNode dummy = {0, NULL};
    struct ListNode* current = &dummy;

    for (int i = 0; i < size; i++) {
        current->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        current->next->val = values[i];
        current->next->next = NULL;
        current = current->next;
    }

    return dummy.next;
}

void printLinkedList(struct ListNode* head) {
    while (head) {
        printf("%d", head->val);
        if (head->next) printf(" -> ");
        head = head->next;
    }
    printf("\n");
}

// Example usage
void test_main() {
    int l1_values[] = {2, 4, 3};
    int l2_values[] = {5, 6, 4};

    struct ListNode* l1 = createLinkedList(l1_values, 3);
    struct ListNode* l2 = createLinkedList(l2_values, 3);

    struct ListNode* result = addTwoNumbers(l1, l2);

    printf("Result: ");
    printLinkedList(result); // Expected Output: 7 -> 0 -> 8
}
