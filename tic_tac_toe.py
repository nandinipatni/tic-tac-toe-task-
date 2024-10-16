def play():
  z = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
  c = 0
  e = 0
  x = 1
  n = 1
  a = "X"
  print("TIC TAC TOE GAME")

  def board():
    print(z[1], "|", z[2], "|", z[3])
    print("________")
    print(z[4], "|", z[5], "|", z[6])
    print("________")
    print(z[7], "|", z[8], "|", z[9])

  while n != 0:
    i = str(input("Do you want to play (yes/no): "))
    if i == "yes":
      if c < 9:
        while x != 0:
          board()
          if c % 2 == 0:
            print("Player X")
          else:
            print("Player 0")

          e = int(input("Enter your move (1-9): "))
          if e < 1 or e > 9 or z[e] != ' ':
            print("Invalid move. Try again.")
            continue

          a = "X" if c % 2 == 0 else "0"
          z[e] = a
          c += 1

          if c >= 5:
            if (z[1] == z[2] == z[3] != ' ' or z[4] == z[5] == z[6] != ' ' or
                z[7] == z[8] == z[9] != ' ' or z[1] == z[4] == z[7] != ' ' or
                z[2] == z[5] == z[8] != ' ' or z[3] == z[6] == z[9] != ' ' or
                z[1] == z[5] == z[9] != ' ' or z[3] == z[5] == z[7] != ' '):
              board()
              print(f"Player {a} Won")
              x = 0
              break

          if c == 9:
            board()
            print("Draw")
            x = 0
            break

      else:
        print("Game over.")
        x = 0

    elif i == "no":
      print("Okay. Thank you.")
      break
    else:
      print("Enter a valid input.")
      continue

play()
