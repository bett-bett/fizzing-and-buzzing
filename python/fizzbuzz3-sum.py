def sum_fizz_buzz (number):
  # simple solution
  # sum=0
  # for i in range (number):
  #   if(i%5==0 or i%3==0):
  #     sum+=i
  # return sum

  # sum is a built in python function, fyi

  # Of interest today is generator expression, look at list comprehension as well
  # Generator expression (expression for item in iterable)
  # create list with a shorter syntax. elements are generated when they are needed, meaning the full lust is not loaded in memory as opposed to list comprehension 
  return sum(
    i for i in range(number) if (i%3==0 or i%5==0)
  )

  # list comprehension
  # return sum([i for i in range(number) if (i % 3 == 0 or i % 5 == 0)])


print(sum_fizz_buzz(11))
