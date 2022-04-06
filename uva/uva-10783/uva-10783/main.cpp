//
//  main.cpp
//  uva-10783
//
//  Created by Arga Roh Sahrijal Saragih on 2/2/22.
//

#include <iostream>

int main(void) {
    // insert code here...
    int n;
    int casenum = 1;
    int a;
    int b;
    int sum = 0;
    std::cin >> n;
    while (casenum <= n) {
        sum = 0;
        std::cin >> a;
        std::cin >> b;
        for (int i = a; i <= b; i++) {
            if (i % 2 == 1) {
                sum += i;
            }
        }
        std::cout << "Case " << casenum++ << ": " << sum << "\n";
    }
    return 0;
}
