def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)
numbers=[1,2,3,4,5]
result=sum_of_squares(numbers)
print(result)