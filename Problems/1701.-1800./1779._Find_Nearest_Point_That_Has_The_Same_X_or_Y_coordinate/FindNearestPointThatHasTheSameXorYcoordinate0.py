#!/bin/python3
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        valid_points = [point for point in points if point[0] == x or point[1] == y]
        manhattan_dist = lambda a: abs(x - a[0]) + abs(y - a[1])
        all_valids = list(map(manhattan_dist, valid_points))

        lst = []
        for j in range(len(valid_points)):
            if all_valids[j] == min(all_valids):
                lst += [points.index(valid_points[j])]
        return min(lst) if lst else -1
