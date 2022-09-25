
def my_sum(*numbers):
    output = 0
    for number in numbers:
        output += number
    print (output)

if __name__ == '__main__':
    my_sum(10,20,30,20)