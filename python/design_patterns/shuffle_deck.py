def shuffleCards(deckSize):
    deck = []
    # Create deck
    for i in range(0, deckSize):
        deck.append(i)

    print ("The initial deck is:", deck)

    done = False
    mainCounter = 0

    # Main loop
    while not done:

        # Split the deck
        upperHalf = []
        lowerHalf = []
        for i in range(0, deckSize // 2):
            upperHalf.append(deck[i])
        for i in range(deckSize // 2, deckSize):
            lowerHalf.append(deck[i])

        # Shuffle the deck
        i = len(deck) - 1
        j = len(upperHalf) - 1
        while i >= 0:
            deck[i] = upperHalf[j]
            i -= 1
            deck[i] = lowerHalf[j]
            i -= 1
            j -= 1

        print("The deck is:", deck)

        # Check for completion
        for i in deck:
            if deck[i] != i:
                done = False
                break
            done = True

        mainCounter += 1
    print("Deck size", deckSize, "# shuffles", mainCounter)

shuffleCards(3)