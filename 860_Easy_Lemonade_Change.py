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
        fives = 0                            # first 3 lines sets counters for the amount of each bill you have
        tens = 0
        twenties = 0
        for x in bills_list:                 # iterates through the list of bills
            if x == 5:                       # if the bill is a five then....
                fives += 1                   # +1 to $5 counter
            elif x == 10:                    # else if bill is a 10 then....
                tens += 1                    # +1 to $10 counter
                fives -= 1                   # -1 from $5 counter because you give back $5 as change
                if fives >= 0:               # you can only give back fives, so check to see if you have negative fives, if so, returns False, else continue
                    continue
                else:
                    return False
            elif x == 20:                    # else if bill is a 20 then....
                twenties += 1                # +1 to $20 counter
                if tens >= 1:                # check to see if you have any $10 bills to use as change. if yes then....
                    tens -= 1                # -1 from $10 counter
                    fives -= 1               # -1 from $5 counter
                    if fives < 0:            # checks to see if you ran out of fives. can't give negative money. if negative, returns False
                        return False
                else:                        # if there are no $10 bills to use as change....
                    fives -= 3               # -3 from $5 counter because you give back $15 in fives
                    if fives < 0:            # checks to see if you ran out of fives. can't give negative money. if negative, returns False
                        return False
        return True                          # if it makes it through the list without hitting a false, then it's True

s = Solution()
payment = [5, 10, 10]  # False
payment2 = [5, 5, 10, 10, 20]  # False
payment3 = [5, 5, 10]  # True
print(s.lemonadeChange(payment))


# All in all, I feel like my answer is pretty rudimentary. Just a bunch of if, elif, else statements to navigate down different branching paths.
# Some paths lead to a 'False' and only one leads to a 'True'. First answers were pretty basic and I didn't realize you could use $10 to make change
# for the $20 payment. I thought the question was a lot easier than it actually is if I only had to make sure I didn't run out of $5 bills hahaha!
