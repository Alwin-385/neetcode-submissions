class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalcost=0
        totalgas=0
        for i in range(len(gas)):
            totalcost+=cost[i]
            totalgas+=gas[i]
        if totalgas<totalcost:
            return -1
        startindex=0
        currentgas=0
        for i in range(len(gas)):
            currentgas+=gas[i]-cost[i]
            if currentgas<0:
                currentgas=0
                startindex=i+1
        return startindex