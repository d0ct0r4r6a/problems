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

  let tc = {
    nDice: null,
    sDices: []
  }
  let index = 0

  rl.on('line', function (line) {
    // TODO: Process input
    if (problem.T === 0) {
      // Get number of test cases from first line
      problem.T = Number(line)
    } else {
      // TODO process the rest of the data
      if (tc.nDice === null) {
        tc.nDice = Number(line)
      } else {
        const sDices = line.split(' ')
        tc.sDices = sDices.map(Number)
      }
    
      if (++index % 2 === 0) {
        problem.testCases.push(tc)
        tc = {
          nDice: null,
          sDices: []
        }
      }
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
  let output = `Case #${tcIndex + 1}: `
  input.sDices.sort((a, b) => a - b)
  let straight = []
  input.sDices.forEach((side, index) => {
    if (index === 0) {
      straight.push(1)
    } else {
      if (side > straight[straight.length - 1]) {
        straight.push(straight.length + 1)
      }
    }
  })
  output += straight.length
  console.log(output)
}

readInput()