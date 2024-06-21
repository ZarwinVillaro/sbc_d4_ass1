import random

print("-" * 50)
try:
    # Pagkuha sa bet gikan sa user input
    bet = list(map(int, input("Bet: ").split()))
    # Generate random result
    result = [random.randint(1, 2) for _ in range(3)]
    # I-print ang resulta ug ang status sa imong bet
    print(f"Result: {result} - {'Win ✓' if bet == result else 'Partially Win!' if sorted(bet) == sorted(result) else 'lose X'}")
except ValueError:
    # I-handle ang sayop nga input
    print("Invalid input. Please enter three numbers separated by spaces.")
print("-" * 50)

#Sa kani na revise code gi remove ra nako ang mga nag balik2 na part sa code para mas concise and accurate and also mas mapa shortin pero gi maintain nako ang functionality.