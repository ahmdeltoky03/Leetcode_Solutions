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
    ListNode* deleteMiddle(ListNode* head) {
        int len=0;
        ListNode *curr=head;
        while(curr != NULL){
            len++;
            curr=curr->next;
        }
        int mid=len/2;
        //list is empty
        if(mid==0)return nullptr;

        
        ListNode *ans=NULL;
        ListNode *_curr=head;
        int i=0;
        while(i<mid){
         ans=_curr;
         _curr=_curr->next;
         i++;
        }
        ans->next=_curr->next;
        return head;
    }
};