'''There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:
n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        tank = 0
        
        while start < len(gas):
            print("start:", start)
            x = start
            x = x % len(gas)

            tank += gas[start]
            print("tank start:", tank)

            while tank >= 0:
                print("curr:", x)
                print("tank:", tank, ", cost:", cost[x])

                tank -= cost[x]
                print("tank:", tank)
                if (tank < 0):
                    break

                x += 1
                x = x % len(gas)
                tank += gas[x]

                if (x == start):
                    return start
                
            tank = 0
            print(x)
            if x - start < 1:
                start += 1
            else:
                start += x - start

            print()
        return -1


test = Solution()

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# print(test.canCompleteCircuit(gas, cost))

# gas = [2,3,4]
# cost = [3,4,3]
# print(test.canCompleteCircuit(gas, cost))

# gas = [5,1,2,3,4]
# cost = [4,4,1,5,1]
# print(test.canCompleteCircuit(gas, cost))

# gas = [5,8,2,8]
# cost = [6,5,6,6]
# print(test.canCompleteCircuit(gas, cost))

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(test.canCompleteCircuit(gas, cost))