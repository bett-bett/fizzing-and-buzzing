function fizzbuzz(n, index=1, answer = []){
  // recursion
  
  if (index>n) return answer
  // console.log(index) 

  // push "Fizz"/"Buzz"/"FizzBuzz" if divisible or number.toString() to the answer array
  answer.push(
    (
      // if 3 then "Fizz" string + none or "Buzz" string if 5
      (index % 3 === 0 ? "Fizz" : "") + (index % 5 === 0 ? "Buzz" : "")
    )  
    || 
    index.toString()
  )

  return fizzbuzz(n, index+1, answer)
}

console.log(fizzbuzz(15))
// console.log(fizzbuzz(365))