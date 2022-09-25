def run_strsort():
   word = input("give me a word:\n")
   output = []
   for letter in word:
       output.append(f'{letter}')

   word =''.join(sorted(output))
   print (word)


if __name__ == '__main__':
    run_strsort()