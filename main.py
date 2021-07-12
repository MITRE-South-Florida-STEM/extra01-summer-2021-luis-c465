# Begin by asking for interval of numbers
min = int(input("Min num? "))
max = int(input("Max num? "))

min_valid = min
max_valid = max

# Start the while loop to guess until correct
while True:
    numbers_list = list(range(min_valid, max_valid + 1))

    array_length = len(numbers_list)
    if array_length == 1: 
        guess = numbers_list[0]
        break

    guess = numbers_list[int(array_length / 2)]
    print(f"Guess: {guess}")
    guess_correctness = input("high/low/correct? ")

    # actual answer is higher than the computer's guess
    if guess_correctness == "h": 
        max_valid = guess - 1
    
    # actual answer is lower than the computer's guess
    elif guess_correctness == "l":
        min_valid = guess + 1

    # computer's guess is correct
    elif guess_correctness == "c":
        break

    else:
        print("Input is invalid\nRetrying ...")
        continue

# Give victory message here
print(f"Computer wins!\nThe guess: {guess} is correct!")