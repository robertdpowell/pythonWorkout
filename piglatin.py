def run_pig():
   string = input("please give me a word")
   if string[0] in 'aeiou':
       print (f'{string}way')
   else:
       print (f'{string[1:]}{string[0]}ay')

def run_pig_sentence():
    sentence = input("please give me a sentence")
    output=[]
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    print(' '.join(output))

if __name__ == '__main__':
    run_pig_sentence()