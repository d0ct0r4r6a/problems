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
      problem.testCases.push(Number(line))
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
  let result = `Case #${tcIndex + 1}: ` + countPalindromicFactors(input)
  console.log(result)
}

function countPalindromicFactors(num) {
  let count = 0
  for (let factor of getFactors(num)) {
    count += isPalindrome(String(factor))
  }
  return count
}

function getFactors(num) {
  let fac = [], i = 1, ind = 0;

  while (i <= Math.floor(Math.sqrt(num))) {
    //inserting new elements in the middle using splice
    if (num%i === 0) {
      fac.splice(ind,0,i);
      if (i != num/i) {
        fac.splice(-ind,0,num/i);
      }
      ind++;
    }
    i++;
  }

  //swapping first and last elements
  let temp = fac[fac.length - 1];
  fac[fac.length - 1] = fac[0];
  fac[0] = temp;

  // nice sorted array of factors
  return fac;
}

function isPalindrome(s,i) {
  return (i=i||0)<0||i>=s.length>>1||s[i]==s[s.length-1-i]&&isPalindrome(s,++i)
}

readInput()