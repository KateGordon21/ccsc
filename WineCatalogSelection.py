"""
Bob was visiting the beautiful Tuscany region of Italy and decided to take a wine testing tour. But before
testing the wines in the restaurant, he wanted to make sure about the price and asked for the price card.
Unfortunately, the card contained all the fancy names of the wines without the price tag. Bob, being
smart, searched with the restaurant name online to get an idea about the price. Interestingly he found N
different versions (old and new) of the price card. Now he decided to apply the following algorithm to
find the most recent price card:
Rule 1: The price card which has the maximum number of wines with the maximum price for that item
among the price cards will be chosen.
Rule 2: In case of multiple price cards with that condition (rule 1), the one with the maximum average
price will be chosen.

Input Format:
● The first line contains two integers x and y that denote the number of price cards and the number of items (wines) on each price card respectively.
● The next x line each contains y integers represented as Pij, the jth price on the ith price card.

Output format
The number of the most recent price card.
It is guaranteed that the answer is unique
"""
def get_max_lists(lists: list(list())) -> list():
    # Keeping track of the list with the maximum amount of maximally-priced wines with a counter of maxes for each list
    max_counter = [0] * len(lists)
    for i in range(len(lists[0])):
        max_price = 0
        for j in range(len(lists)):
            max_price = max(lists[j][i], max_price)
        
        for j in range(len(lists)):
            if lists[j][i] == max_price:
                max_counter[j] += 1

    max_value = max(max_counter)
    max_lists = []
    for i in range(len(max_counter)):
        if max_counter[i] == max_value:
            max_lists.append(i)

    return max_lists

def get_highest_average(lists):
    highest_average = 0
    highest_average_list = 0
    for key in lists:
        if sum(lists[key]) // len(lists[key]) > highest_average:
            highest_average = sum(lists[key]) // len(lists[key])
            highest_average_list = key

    return highest_average_list
    
if __name__ == "__main__":

    # Getting user input
    x, y = input().split()
    x, y = int(x), int(y)
    lines = []
    
    count = 0
    while count < x:
        current_list = input().split()

        if len(current_list) > y or len(current_list) < y:
            continue

        for i in range(len(current_list)):
            current_list[i] = int(current_list[i])

        lines.append(current_list)
        count += 1

    # Getting the lists with the highest priced wines
    max_lists = get_max_lists(lines)
    
    # If there is more than 1 list with the most highest priced wines (a tie), the take the list with the highest average
    if len(max_lists) > 1:

        # Get the lists for the wines with the max count
        maximum_priced_wine_lists = dict()
        for i in max_lists:
            maximum_priced_wine_lists[i] = lines[i]

        highest_average_list = get_highest_average(maximum_priced_wine_lists)
        print(highest_average_list+1)

    else:
        print(max_lists[0]+1)