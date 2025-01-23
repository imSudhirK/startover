# Gas Station
# https://leetcode.com/problems/gas-station/description

def canCompleteCircuit(gas, cost):
    num_station = len(gas)
    total_gas_surplus = 0
    start_index, current_surplus = 0, 0
    for i in range(num_station):
        gas_diff  = gas[i] - cost[i]
        total_gas_surplus += gas_diff
        current_surplus += gas_diff
        if current_surplus < 0:
            current_surplus = 0
            start_index = i + 1
    if total_gas_surplus < 0:
        return -1
    return start_index

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))