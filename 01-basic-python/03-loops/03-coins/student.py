# Write your code here


def coins(one, two, five, goal):
# Calculate the maximum amount of money that can be formed
    max_amount = one + 2 * two + 5 * five

    # Check if the goal amount is achievable
    if goal <= max_amount:
        # Calculate the maximum number of 5 coins needed
        max_fives_needed = min(five, goal // 5)
        
        # Iterate over the number of 5 coins used
        for fives_used in range(max_fives_needed + 1):
            # Calculate the remaining amount after using 5 coins
            remaining_after_fives = goal - 5 * fives_used
            
            # Calculate the maximum number of 2 coins needed
            max_twos_needed = min(two, remaining_after_fives // 2)
            
            # Check if the remaining amount is achievable using 2 and 1 coins
            if remaining_after_fives - 2 * max_twos_needed <= one:
                return True

    return False