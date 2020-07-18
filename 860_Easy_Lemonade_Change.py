# Level: Easy
# 860. Lemonade Change

# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
# Note that you don't have any change in hand at first.
# Return true if and only if you can provide every customer with correct change.

# Example 1:
# Input: [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# Example 2
# Input: [10,10]
# Output: false


class Solution:
    def lemonadeChange(self, bills_list):
        fives = 0
        tens = 0
        twenties = 0
        for x in bills_list:
            print(x)
            if x == 5:
                fives += 1
            elif x == 10:
                tens += 1
                fives = fives - 1
                if fives >= 0:
                    continue
                else:
                    return False
            elif x == 20:
                twenties += 1
                if tens >= 1:
                    tens = tens - 1
                    fives = fives - 1
                    if fives < 0:
                        return False
                else:
                    fives = fives - 3
                    if fives < 0:
                        return False
#        if fives >= 0 and tens >= 0 and twenties >= 0:
        return True


s = Solution()

payment = [5, 10,10]

print(s.lemonadeChange(payment))

