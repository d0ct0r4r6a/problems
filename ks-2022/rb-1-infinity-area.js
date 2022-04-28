const readline = require('readline')

function readInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  })

  let problem = {
    T: 0,
    testCases: []
  }

  rl.on('line', function (line) {
    // TODO: Process input
    if (problem.T === 0) {
      // Get number of test cases from first line
      problem.T = Number(line)
    } else {
      // TODO process the rest of the data
      const [r, a, b] = line.split(' ')
      problem.testCases.push([Number(r), Number(a), Number(b)])
    }
  })

  .on('close', () => {
    // Finished processing input, now solve question
    solveProblem(problem)
    process.exit()
  })
}

function solveProblem(problem) {
  problem.testCases.forEach((input, tcIndex) => {
    solveTestCase(input, tcIndex)
  })
}

function solveTestCase(input, tcIndex) {
  let [R, A, B] = input
  let result = `Case #${tcIndex + 1}: `
  let totalAllArea = 0
  do {
    totalAllArea += calculateBothCircleArea(R, A)
    R = Math.floor(R * A / B)
  } while (R)
  result += totalAllArea.toFixed(6)
  console.log(result)
}

function calculateArea(radius) {
  return Math.PI * radius * radius
}

function calculateBothCircleArea(R, A) {
  return calculateArea(R) + calculateArea(R * A)
}

readInput()