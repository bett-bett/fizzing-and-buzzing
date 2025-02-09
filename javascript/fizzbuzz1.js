function fizzbuzz(n){
  // switch statements instead of if...else statements
  const answer=[]
  for (i=1; i<=n; i++){
    switch(true){
      case(i%3===0 && i%5==0):
        answer.push("FizzBuzz")
        break;
      case(i%3==0):
        answer.push("Fizz")
        break;
      case(i%5===0):
        answer.push("Buzz")
        break;
      default:
        answer.push(i.toString())
    }
  }
  return answer
}

console.log(fizzbuzz(15))
// console.log(fizzbuzz(365))
