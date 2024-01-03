#!/bin/python3

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank_floor, total_lasers = [], 0

        for cell in bank:
            num_devices = cell.count("1")
            if (num_devices > 0):
                bank_floor += [num_devices]

        for i in range(len(bank_floor)-1):
            total_lasers += bank_floor[i]*bank_floor[i+1]
        return total_lasers
