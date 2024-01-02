""""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.
"""
def minion_game(s):
    a, b, n = 0, 0, len(s)
    
    for i in range(n):
        if s[i] in "AEIOU":
            a += n-i
            print(a,s[i])
            continue
        b += n-i
        print(b, s[i])

    print(f'Kevin {a}' if a>b else f'Stuart {b}' if a!=b else 'Draw')

minion_game("BANANA")


# for i in range(4):
#    for j in range(4):
#       print(i,j)

def get_all_substrings(string):
  """Returns a list of all possible substrings of the given string."""
  substrings = []
  for i in range(len(string)):
    for j in range(i, len(string)):
      substrings.append(string[i:j + 1])
  return substrings

# print(get_all_substrings("BANANA"))



# string= "BANANA"
# substrings = []
# for i in range(len(string)):
#     print(i)
#     for j in range(i, len(string)):
#         print(i,j)
#         substrings.append(string[i:j + 1])
#     print(substrings)




# def minion_game(string):
#     pass
# words = []
# word =""
# string = "Banana".upper()
# vowels = "aeiou".upper()

# for i in string:
#     if i in vowels:
#         word+= len(string) + i
#         print(word)
  
# print(words) 