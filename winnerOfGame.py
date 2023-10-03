# -*- coding: utf-8 -*-
"""LeetCodeProblems.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EhXHTo5IVZOHKp27uxh1iG6lWh_PX7WG
"""

class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        if len(colors) < 3:
            return False
        elif len(colors) == 3 and colors[1] != 'A':
            return False
        elif len(colors) == 3 and colors[1] == 'A' and (colors[0] != 'A' or colors[2] != 'A'):
            return False
        elif len(colors) == 3 and colors[1] == 'A' and colors[0] == 'A' and colors[2] == 'A':
            return True

        Alice = 0
        Bob = 0
        for i in range(1,len(colors) - 1):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                Alice = Alice + 1
            elif colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                Bob = Bob + 1

        if Alice > Bob:
            return True
        else:
            return False