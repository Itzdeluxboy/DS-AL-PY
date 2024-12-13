'''0-1 Knapsack Problem
Problem statement
You’re in charge of selecting a football (soccer) team from a large pool of players. Each player has a cost, and a rating. You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there’s no minimum or maximum team size.'''
def knapsack(players, budget):
    n = len(players)
    dp = [[0] * (budget + 1) for i in range(n + 1)]

    for j in range(1, n + 1):
        cost, rating = players[j - 1]
        for w in range(budget + 1):
            if cost <= w:
                # Select the maximum of not picking the item or picking it
                dp[j][w] = max(dp[j - 1][w], dp[j - 1][w - cost] + rating)
            else:
                dp[j][w] = dp[j - 1][w]

    return dp[n][budget]

def run_tests():
    # Test case 1 : All elements can be included
    players1 = [(5, 10), (4, 40), (6, 30), (3, 50)]  
    budget1 = 20  
    print("Test case 1")
    print("Players:", players1)  
    print("Budget:", budget1)  
    print("Highest Total Rating:", knapsack(players1, budget1))  

    # Test case 2: None of the elements can be included
    players2 = [(15, 40), (25, 50), (35, 60)]  
    budget2 = 10  
    print("\nTest case 2")
    print("Players:", players2)  
    print("Budget:", budget2)  
    print("Highest Total Rating:", knapsack(players2, budget2))  

    # Test case 3: Only one of the elements can be included
    players3 = [(10, 20), (20, 40), (30, 60)]  
    budget3 = 15  
    print("\nTest case 3")
    print("Players:", players3)  
    print("Budget:", budget3)  
    print("Highest Total Rating:", knapsack(players3, budget3))  

    # Test case 4: Generic case with mixed inclusion
    players4 = [(5, 50), (8, 60), (3, 40), (6, 70)]  
    budget4 = 15  
    print("\nTest case 4")
    print("Players:", players4)  
    print("Budget:", budget4)  
    print("Highest Total Rating:", knapsack(players4, budget4))  

run_tests()

#Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.
def knapsack2(profit, weight, capacity):
    n = len(profit)
    dp = [[0] * (capacity + 1) for i in range(n+1)]

    for j in range(1, n+1):
        for w in range(capacity + 1):
            if weight[j-1] <=w:

                dp[j][w] = max(dp[j-1][w], dp[j-1][w - weight[j-1]] + profit[j-1])
            else:
                dp[j][w] = dp[j-1][w]
        return dp[n][capacity]
    
def run_tests():
    profit = [2,3,1,5,4,7]
    weight = [4,5,1,3,2,5]
    capacity = 15

    print("Test Case")
    print("Profit:", profit)
    print("Weight:", weight)
    print("Capacity:", capacity)
    print("Maximum Profit:", knapsack2(profit, weight, capacity))

run_tests()