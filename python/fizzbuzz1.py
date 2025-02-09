def fizzbuzz(n):
  answer=[]
  for i in range(1, n+1, 1):
    # note range(2) is 0,1
    if (i%3==0 and i%5==0):
      # FizzBuzz
      answer.append('FizzBuzz')
    else:
      if(i%3==0):
        # Fizz
        answer.append('Fizz')
      elif(i%5==0):
        # Buzz
        answer.append('Buzz')
      else:
        # i
        answer.append(f'{i}')
  return answer

print(fizzbuzz(365))