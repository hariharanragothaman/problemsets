def countIterations(deckSize):
    deck = []

    # Create deck
    for i in range(1, deckSize+1):
        deck.append(i)
    print("The initial deck is:", deck)

    original_deck = deck

    done = False
    mainCounter = 0

    # Main loop
    while not done:

        stack = []
        length = len(deck)
        for i in range(0, len(deck)):
            if i % 2 == 0:
                stack.append(deck[i])

        print("The stack is:", stack)



        mainCounter += 1
    print("Deck size", deckSize, "# shuffles", mainCounter)

countIterations(10)