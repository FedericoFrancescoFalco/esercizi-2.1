class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> list[int]:
    prev = None
    current = head
        
 
    while current is not None:
        next_node = current.next  
        current.next = prev       
        prev = current
        current = next_node
        
    reversed_head = prev
    
    result = []

    while reversed_head is not None:
        result.append(reversed_head.val)
        reversed_head = reversed_head.next
        
    return result











def anagram(s: str, t: str) -> bool:
    s= s.lower()
    t= t.lower()
    return sorted(s)==sorted(t)









def word_break(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) +1):
        for word in word_set:
          if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                break
    
   
    return dp[-1]


