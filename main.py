import random

def retrieve_nfaces(): # Function retrieves inputted number of faces from keyboard
  gotDataCorrectly = False
  while gotDataCorrectly == False:
    print("Please enter the number of faces")
    try: # Testing for invalid (non integer) input
      nfaces = int(input())
      if nfaces >= 0:
        return nfaces
      else: 
        print("nfaces should be positive!")
        gotDataCorrectly = False
    except (ValueError, SyntaxError):
      print("nfaces should be a number")
      gotDataCorrectly = False

def retrieve_nthrows(nfaces): # Function retrieves inputted number of throws from keyboard
  gotDataCorrectly = False
  print("Please enter the number of throws")
  while gotDataCorrectly == False: 
    try: # Testing for invalid (non integer or non multiple) input
      nthrows = int(input())
      if nthrows % nfaces == 0 and nthrows >= 0:
        gotDataCorrectly = True
        return nthrows
      else:
        print("nthrows should be a positive multiple of nfaces!")
        gotDataCorrectly = False
    except (ValueError, SyntaxError):
      print("nthrows should be a number!")
      gotDataCorrectly = False

def main():
  nfaces = retrieve_nfaces()
  nthrows = retrieve_nthrows(nfaces)
  roll = []
  result = []
  for counter1 in range(nthrows): # Loops through throws and simulates each roll
    roll.append(random.randrange(1, nfaces + 1)) # Stores rolls in list
  for nfaces_loop in range(1, nfaces + 1): # Loops through dice faces
    result.append(0) # Creates empty list of correct dimensions
    for roll_loop in roll: # Loops through rolls and compares to faces from above loop
      if roll_loop == nfaces_loop: 
        result[nfaces_loop - 1] += 1
    print("Face ", nfaces_loop, " came up ", result[nfaces_loop - 1]," times.") # Prints during loop

if __name__ == "__main__":
  main()