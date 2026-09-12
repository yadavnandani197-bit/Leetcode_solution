class Solution(object):
    def maximumWeight(self, intervals):
        import bisect
        arr = [] 
        for idx, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, idx))
        arr.sort(key=lambda x: x[0]) 

        n = len(arr)
        L = [arr[i][0] for i in range(n)]
        R = [arr[i][1] for i in range(n)]
        W = [arr[i][2] for i in range(n)]
        ORIG = [arr[i][3] for i in range(n)]

        nxt = [n]*n
        for i in range(n):
            j = bisect.bisect_right(L, R[i], lo=i+1)
            nxt[i] = j

        
        dp_w = [[0]*5 for _ in range(n+1)]
        dp_seq = [[() for _ in range(5)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            oi = ORIG[i]
            ni = nxt[i]
            wi = W[i]
            for k in range(1, 5):
                
                w_skip = dp_w[i+1][k]
                seq_skip = dp_seq[i+1][k]

                
                w_take = wi + dp_w[ni][k-1]
                seq_prev = dp_seq[ni][k-1]
                
                lst = list(seq_prev)
                bisect.insort(lst, oi)
                seq_take = tuple(lst)

                if w_take > w_skip:
                    dp_w[i][k] = w_take
                    dp_seq[i][k] = seq_take
                elif w_take < w_skip:
                    dp_w[i][k] = w_skip
                    dp_seq[i][k] = seq_skip
                else: 
                    if seq_take < seq_skip:
                        dp_w[i][k] = w_take
                        dp_seq[i][k] = seq_take
                    else:
                        dp_w[i][k] = w_skip
                        dp_seq[i][k] = seq_skip

        return list(dp_seq[0][4])