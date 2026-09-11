class Solution(object):
    def countGroups(self, position, speed, distance):
        n = len(position)
        if n <= 1:
            return n

        # Phase 1: merge at t=0 where gap <= distance
        init_pos = []
        init_speed = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and position[j+1] - position[j] <= distance:
                j += 1
            # group i..j -> leader j
            init_pos.append(position[j])
            init_speed.append(speed[j])
            i = j + 1

        m = len(init_pos)
        # Phase 2: from right to left, survivor must have increasing speed
        # survivors[0] is closest ahead
        survivors_speed = [init_speed[-1]]
        # survivors_pos not needed for final count, but keep for clarity
        # we only need speeds after phase 1 because gaps > distance

        for idx in range(m-2, -1, -1):
            s = init_speed[idx]
            # next survivor ahead
            next_s = survivors_speed[0]
            if s <= next_s:
                # never catches
                survivors_speed.insert(0, s)
            else:
                # catches and merges, no new group
                pass

        return len(survivors_speed)
        