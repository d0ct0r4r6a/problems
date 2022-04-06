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
    n: null,
    fArr: [],
    pArr: []
  }
  let index = 0

  rl.on('line', function (line) {
    // TODO: Process input
    if (problem.T === 0) {
      // Get number of test cases from first line
      problem.T = Number(line)
    } else {
      // TODO process the rest of the data
      if (tc.n === null) {
        tc.n = Number(line)
      } else if (tc.fArr.length === 0 ) {
        tc.fArr = line.split(' ').map(Number)
      } else {
        tc.pArr = line.split(' ').map(Number)
      }

      if (++index % 3 === 0) {
        problem.testCases.push(tc)
        tc = {
          n: null,
          fArr: [],
          pArr: []
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
  const initiators = getInitiators(input)
  let maxFuns = []
  initiators.forEach(initIndex => {
    maxFuns.push(calcMaxFun(input, initIndex, initiators))
  })
  output += Math.max(...maxFuns)
  console.log(output)
}

function getInitiators(input) {
  let initiators = []
  Array(input.n).fill(1).forEach((i, index) => {
    initiators.push(index)
  })
  input.pArr.forEach((p) => {
    initiators = initiators.filter(init => init !== p - 1)
  })
  return initiators
}

function calcFun(input, currentIndex, naIndices = []) {
  const currentValue = input.fArr[currentIndex]
  const nextF = input.pArr[currentIndex] - 1
  if (nextF < 0 || naIndices.includes(nextF)) {
    return {
      value: currentValue,
      naIndices
    }
  } else {
    naIndices.push(nextF)
    const { value: inValue, naIndices: inNaIndices } = calcFun(input, nextF, naIndices)
    return {
      value: Math.max(currentValue, inValue),
      naIndices: Array.from(new Set([...naIndices, ...inNaIndices]))
    }
  }
}
function calcMaxFun(input, initIndex, initiators = [], naIndices = []) {
  const { value, naIndices: newNaIndices } = calcFun(input, initIndex, naIndices)
  initiators = initiators.filter(i => i !== initIndex)
  if (initiators.length === 0) {
    return value
  } else {
    let maxFunArr = []
    initiators.forEach(i => {
      const maxFun = calcMaxFun(input, i, initiators, [...naIndices, ...newNaIndices])
      maxFunArr.push(maxFun)
    })
    return value + Math.max(...maxFunArr)
  }
}

readInput()