import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function FizzBuzz(num){
  // if (num == 0) return num
  // else if (num % 15 == 0) return "FizzBuzz"
  // else if (num % 3 == 0 ) return "Fizz"
  // else if (num % 5 == 0 ) return "Buzz"
  // return num

  return num == 0 
  ? num 
  : ((num % 3 == 0 ? "Fizz":"") + (num % 5 == 0 ? "Buzz":"") || num)
}

function App() {
  const [count, setCount] = useState(0)
  function handleClick(){
    setCount(count + 1)
  }
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Count is FizzBuzz</h1>
      <div className="card">
        <button onClick={handleClick}>
          count is {FizzBuzz(count)}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
