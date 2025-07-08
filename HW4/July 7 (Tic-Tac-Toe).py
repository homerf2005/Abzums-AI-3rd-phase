import random
res = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
curr = ("", "")


def show_res(res):
    print(res[0], end=" | ")
    print(res[1], end=" | ")
    print(res[2])
    print(res[3], end=" | ")
    print(res[4], end=" | ")
    print(res[5])
    print(res[6], end=" | ") # eofheojrhouhnoerhuof
    print(res[7], end=" | ")
    print(res[8])


def symbol_and_first():
    global a, b, curr
    while True:
        a = input("Hey player 1, choose your symbol (X/O). \n")
        a = a.upper()
        if a not in ("X", "O"):
            print("Invalid input, try again. \n")
        else:
            break
    print(f"Ok, player 1 is {a}")
    if a == "O":
        b = "X"
        print("Player 2 is X")
    else:
        b = "O"
        print("Player 2 is O")

    a = (1, a)
    b = (2, b)

    x = random.randint(1, 2)
    print(f"Player {x} is first")
    curr = a if x == 1 else b


def winner(res):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for i, j, k in win_combinations:
        if res[i] == res[j] == res[k] != "-":
            return True
    return False


def turn():
    global a, b, curr
    while True:
        try:
            p1 = int(input(f"Player {curr[0]}, your turn.\n"))
        except ValueError:
            print("Enter a valid number")
            continue
        if p1 in range(1, 10) and res[p1 - 1] == "-":
            res[p1 - 1] = curr[1]
            show_res(res)
            break
        elif p1 in range(1, 10):
            print(f"{p1} is chosen. Try another one")
            show_res(res)
        else:
            print("your input is not in range 1 to 9, try again.")

    curr = b if curr == a else a


show_res(res)
symbol_and_first()

count = 0
while True:
    turn()
    if winner(res):
        curr = a if curr == b else b
        print(f"Player {curr[0]} won!")
        break
    count += 1
    if count == 9:
        break
if count == 9:
    print("It's a draw!")
