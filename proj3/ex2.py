import numpy as np
import heapq

filename = "ex2.txt"


# wrapper to get score from
# hash representing upper triangular matrix
def get_score(x, y):
    return 1 if x == y else -2


# outputs the alignment given
# backtrack matrix, input strings and node in table
# to start from
def output_align(backtrack, v, w, i, j):
    v_alignment = ''
    w_alignment = ''
    
    # uses this construct to avoid
    # deep recursion limit
    while True:
        if j == 0:
            return v_alignment, w_alignment
        if backtrack[i,j] == 'dn':
            i, v_alignment, w_alignment = i-1, v[i-1] + v_alignment, '-' + w_alignment
        elif backtrack[i,j] == 'rt':
            j, v_alignment, w_alignment = j-1, '-' + v_alignment, w[j-1] + w_alignment
        else:
            i, j, v_alignment, w_alignment = i-1, j-1, v[i-1] + v_alignment, w[j-1] + w_alignment


# computes global alignment
# for strings v and w using dynamic programming
# and gap penalty sigma
def global_align(v, w, sigma):
    nv = len(v)
    nw = len(w)

    # initialize dp score and backtrack matrices
    s = np.zeros((nv + 1, nw + 1))
    backtrack = np.zeros((nv + 1, nw + 1), np.dtype('a2'))

    # fill in the dp matrices
    for i in xrange(0,nv+1):
        for j in xrange(0, nw+1):
            # use a heap to find max choice
            choices = []

            # use -score since heap keeps min in root
            if i > 0:
                heapq.heappush(choices, (-(s[i-1,j] + sigma), 'dn'))

            if j > 0:
                heapq.heappush(choices, (-(s[i,j-1] + sigma), 'rt'))

            if i>0 and j>0:
                score = get_score(v[i-1], w[j-1])
                heapq.heappush(choices, (-(s[i-1,j-1] + score), 'di'))

            if len(choices) > 0:
                choice = choices[0]
                s[i,j] = -choice[0]
                backtrack[i,j] = choice[1]

    score = s[nv, nw]
    return int(score), backtrack, s


# read data
def readdat(filename):
    with open(filename, 'r') as f:
        v = f.readline().strip()
        w = f.readline().strip()
    return v,w


def main(filename):
    v,w  = readdat(filename)
    score, backtrack, score_matrix = global_align(v, w, -2)

    max_col = -1
    max_value = -999
    i = 0
    for s in score_matrix[len(v)]:
        if s > max_value:
            max_value = s
            max_col = i
        i += 1

    v_alignment, w_alignment = output_align(backtrack, v, w, len(v), max_col)
    print score
    print v_alignment
    print w_alignment

main(filename)
# if __name__ == '__main__' and 'get_ipython' not in dir():
#     filename = sys.argv[1]
#     main(filename)