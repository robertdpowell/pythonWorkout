# def firstlast(sequence):
#    return sequence[:1] + sequence[-1:]
# print (firstlast('abcd'))

# def even_odd_sums (sequence):
#    odd = sum(sequence[1::2]) # start from index 1, end at the end of list and increase each step by 2
#    even =  sum(sequence[0::2]) # start from index 0, end at the end of list and increase each step by 2
#    return (odd, even)
# print (even_odd_sums([10, 20, 30, 40, 50, 60]))

def add_subtract_sums (sequence):
   total = sum(sequence[0:2])
   return (total)
print (add_subtract_sums([10, 20, 30, 40, 50, 60]))

