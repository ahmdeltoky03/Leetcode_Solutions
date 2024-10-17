/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode * revList(ListNode *head){
        ListNode *prev=nullptr;
        while(head){
            ListNode *temp=head->next;
            head->next=prev;
            prev=head;
            head=temp;

        }
        return prev;
    }
    ListNode* removeNodes(ListNode* head) {
         ListNode *rhead=revList(head);
         ListNode *ptr=rhead;
         while(ptr){
            int mx=ptr->val;
            ListNode *temp=ptr->next;
            while(temp && temp->val<mx )temp=temp->next;
            ptr->next=temp;
            ptr=ptr->next;
         }
         return revList(rhead);
    }
};