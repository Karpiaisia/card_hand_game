def score_hand(hand):
        suits = []  # Create an array for suits
        numbers = []  # Create an array for numbers

        for card in hand:  # Create an array for suits
            numbers.append(card.value)
        for card in hand:  # Create an array for numbers
            suits.append(card.suit)

        flush = [suits.count(i) for i in suits]  # This counts all the duplicates in suits
        multinum = [numbers.count(i) for i in numbers]  # This counts all the duplicates in numbers
        difference = max(numbers) - min(numbers)  # Counts the difference between max and min number
        inOrder = sorted(numbers, reverse=False)  # Sort the numbers for easier use.
        highCard = inOrder[-1]  # Take the last (highest) number.



        if 5 in flush:
            if sorted(numbers) == [9, 10, 11, 12, 13]:  # Check if the hand is a royal flush.
                print("Royal flush!")
            elif difference == 4 and max(multinum) == 1:    # If difference is 4 and no duplicate cards,
                print("Straight flush!")                   # it means that the hand is straight.
            elif 1 in numbers:
                print("Flush with Ace high!!")
            else:
                print("Flush with " + highCard + " high!")

        elif 4 in multinum:  # If there are 4 duplicates, it means 4 of a kind.
            print("Four of a kind!")

        elif sorted(multinum) == [2, 2, 3, 3, 3]:  # has to be sorted to check easily.
            print("Full house!")        # a pair and a triple makes full house.

        elif 3 in multinum:  # Checks if there's a triple. Has to be checked after full house.
            print("3 of a kind!")

        elif multinum.count(2) == 4:  # Counts the 2's of the multinum variable.
            print("Two pairs!!")    # if there are 4 times 2, it means there are two pairs.

        elif multinum.count(2) == 2:  # Check if there's only one pair.
            print("Pair!!")

        elif difference == 4:  # If the difference is 4 and no duplicates, it has to be straight.
            print("Straight!!")

        elif 1 in numbers:  # Since 1 means ace, it needs to be checked separately for high card.
            print("Ace high!")

        else:
            print("High card with number: " + str(highCard))

        print("\n")