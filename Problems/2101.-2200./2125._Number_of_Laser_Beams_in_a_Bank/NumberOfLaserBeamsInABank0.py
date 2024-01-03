#!/bin/python3

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank_floor = list(map(self.countOne, bank))
        sec_devices = self.removeZeros(bank_floor)

        laser_beam = 0
        if len(sec_devices) == 1:
            return laser_beam
        else:
            for i in range(0, len(sec_devices)-1):
                laser_beam += (sec_devices[i]*sec_devices[i+1])
        return laser_beam

    # Remove rows with no security device
    def removeZeros(self, list_num: list) -> list:
        while 0 in list_num:
            list_num.remove(0)
        return list_num

    # Number of security devices
    def countOne(self, bin_string: str) -> int:
        return sum([1 for _ in bin_string if _ == "1"])
