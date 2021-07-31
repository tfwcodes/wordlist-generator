import itertools
import os


chrs = input("Enter the characters: ")
n = input("What is the maximum password length: ")
wordlist5 = input("Enter the path to the wordlist to write: ")

File = open(os.path.join(wordlist5), "w")

counter = 0

for xs in itertools.product(chrs, repeat=int(n)):
   word = ''.join(xs)
   File.write(word)
   File.write("\n")




File.close()