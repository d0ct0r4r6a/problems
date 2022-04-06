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
  let printers = [];
  let index = 0;

  rl.on('line', function (line) {
    // TODO: Process input
    if (problem.T === 0) {
      // Get number of test cases from first line
      problem.T = Number(line)
    } else {
      // TODO process the rest of the data
      const printer = line.split(' ')
      printers.push(printer.map(Number))
    
      if (++index % 3 === 0) {
        problem.testCases.push(printers)
        printers = [];
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
  for (let printer of input) {
    if (printer.reduce((acc, curr) => acc + curr) < 1000000) {
      output += 'IMPOSSIBLE'
      console.log(output)
      return
    }
  }
  const validValues = findValidValues(findMaxCMYK(input))
  if (validValues) {
    output += validValues.join(' ')
  } else {
    output += 'IMPOSSIBLE'
  }
  console.log(output)
}

function findMaxCMYK(input) {
  const [p1, p2, p3] = input
  const [c1, m1, y1, k1] = p1
  const [c2, m2, y2, k2] = p2
  const [c3, m3, y3, k3] = p3
  let cMax, mMax, yMax, kMax
  cMax = c2 < c1 ? (c3 < c2 ? c3 : c2) : (c3 < c1 ? c3 : c1)
  mMax = m2 < m1 ? (m3 < m2 ? m3 : m2) : (m3 < m1 ? m3 : m1)
  yMax = y2 < y1 ? (y3 < y2 ? y3 : y2) : (y3 < y1 ? y3 : y1)
  kMax = k2 < k1 ? (k3 < k2 ? k3 : k2) : (k3 < k1 ? k3 : k1)
  return [cMax, mMax, yMax, kMax]
}

function findValidValues(maxValues) {
  const [cMax, mMax, yMax, kMax] = maxValues
  const targetSum = 1000000
  let c = 0, m = 0, y = 0, k = 0
  let isCMax, isMMax, isYMax,isKMax, sum
  isCMax = c === cMax
  isMMax = m === mMax
  isYMax = y === yMax
  isKMax = k === kMax
  while (c <= cMax && m <= mMax && y <= yMax && k <= kMax && sum !== targetSum) {
    sum = c + m + y + k
    if (sum < targetSum && !isCMax) {
      c++
      sum = c + m + y + k
    }
    if (sum < targetSum && !isMMax) {
      m++
      sum = c + m + y + k
    }
    if (sum < targetSum && !isYMax) {
      y++
      sum = c + m + y + k
    }
    if (sum < targetSum && !isKMax) {
      k++
      sum = c + m + y + k
    }
    isCMax = c === cMax
    isMMax = m === mMax
    isYMax = y === yMax
    isKMax = k === kMax
    if (isCMax && isMMax && isYMax && isKMax && sum !== targetSum) {
      return null
    }
  }

  return [c, m, y, k]
}

readInput()
