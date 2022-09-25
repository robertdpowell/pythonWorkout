def run_ubbidubbi():
   word = input("give me a word:\n")
   output = []
   for letter in word:
       if letter in 'aeiou':
           output.append(f'ub{letter}')
       else:
           output.append(letter)
   word =''.join(output)
   print (word)


if __name__ == '__main__':
    run_ubbidubbi()