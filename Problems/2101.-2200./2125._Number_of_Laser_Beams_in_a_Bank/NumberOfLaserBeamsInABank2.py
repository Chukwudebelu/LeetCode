#!/bin/python3

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank_floor = list()

        for cell in bank:
            num_devices = cell.count("1")
            if num_devices != 0:
                bank_floor.append(num_devices)

        i, laser_beams = 0, 0
        while (i < len(bank_floor)-1):
            laser_beams += bank_floor[i]*bank_floor[i+1]
            i += 1
        return laser_beams
