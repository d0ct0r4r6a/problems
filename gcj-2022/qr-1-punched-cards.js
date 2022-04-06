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
      const [a, b] = line.split(' ')
      const aNum = Number(a)
      const bNum = Number(b)

      problem.testCases.push([aNum, bNum])
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
  const [R, C] = input
  const lines = [];
  console.log(`Case #${tcIndex + 1}:`)
  for (let r = 0; r < R; r++) {
    var currentRow = ['', ''];
    for (let c = 0; c < C; c++) {
      if (r === 0 && c === 0) {
        currentRow[0] += '..'
        currentRow[1] += '..'
      } else {
        currentRow[0] += '+-'
        currentRow[1] += '|.'
      }
    }
    lines.push(currentRow);
  }
  for (let i = 0; i < lines.length; i++) {
    console.log(lines[i][0] + '+')
    console.log(lines[i][1] + '|')

    if (i === lines.length - 1) {
      let closing = ''
      for (let c = 0; c < C; c++) {
        closing += '+-'
        if (c === C-1) {
          closing += '+'
        }
      }
      console.log(closing)
    }
  }
}

readInput()