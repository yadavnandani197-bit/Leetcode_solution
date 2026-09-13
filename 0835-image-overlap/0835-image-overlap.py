class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        from collections import defaultdict
        count = defaultdict(int)
        max_overlap = 0

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x1 - x2, y1 - y2)
                count[shift] += 1
                if count[shift] > max_overlap:
                    max_overlap = count[shift]

        return max_overlap