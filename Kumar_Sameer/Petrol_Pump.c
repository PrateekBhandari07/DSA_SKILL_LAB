#include <stdio.h>

int startStation(int gas[], int cost[], int n) {
    int startIdx = -1;
    for (int i = 0; i < n; i++) {
        int currGas = 0;
        int flag = 1;
        for (int j = 0; j < n; j++) {
            int idx = (i + j) % n;
            currGas = currGas + gas[idx] - cost[idx];
            if (currGas < 0) {
                flag = 0;
                break;
            }
        }
        if (flag) {
            startIdx = i;
            break;
        }
    }
    return startIdx;
}

int main() {
    int gas[] = {1, 2, 3, 4, 5};
    int cost[] = {3, 4, 5, 1, 2};
    int n = sizeof(gas) / sizeof(gas[0]);
    printf("%d\n", startStation(gas, cost, n));
    return 0;
}
