class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        l = [amount+1]*(amount+1)
        l[0]=0
        for i in range(1,len(l)):
            for c in coins:
                if i-c >=0:
                    l[i]= min(l[i], 1 + l[i-c])
        if l[amount]!= amount+1:
            return l[amount]
        return -1
      