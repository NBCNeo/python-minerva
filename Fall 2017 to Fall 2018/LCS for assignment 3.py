def LCS_length(X,Y):
    m = len(X)
    n = len(Y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c

S0 = [0,'CAGCGGGTGCGTAATTTGGAGAAGTTATTCTGCAACGAAATCAATCCTGTTTCGTTAGCTTACGGACTACGACGAGAGGGTACTTCCCTGATATAGTCAC']
S1 = [1,'CAAGTCGGGCGTATTGGAGAATATTTAAATCGGAAGATCATGTTACTATGCGTTAGCTCACGGACTGAAGAGGATTCTCTCTTAATGCAA']
S2 = [2,'CATGGGTGCGTCGATTTTGGCAGTAAAGTGGAATCGTCAGATATCAATCCTGTTTCGTAGAAAGGAGCTACCTAGAGAGGATTACTCTCACATAGTA']
S3 = [3,'CAAGTCCGCGATAAATTGGAATATTTGTCAATCGGAATAGTCAACTTAGCTGGCGTTAGCTTTACGACTGACAGAGAGAAACCTGTCCATCACACA']
S4 = [4,'CAAGTCCGGCGTAATTGGAGAATATTTTGCAATCGGAAGATCAATCTTGTTAGCGTTAGCTTACGACTGACGAGAGGGATACTCTCTCTAATACAA']
S5 = [5,'CACGGGCTCCGCAATTTTGGGTCAAGTTGCATATCAGTCATCGACAATCAAACACTGTTTTGCGGTAGATAAGATACGACTGAGAGAGGACGTTCGCTCGAATATAGTTAC']
S6 = [6,'CACGGGTCCGTCAATTTTGGAGTAAGTTGATATCGTCACGAAATCAATCCTGTTTCGGTAGTATAGGACTACGACGAGAGAGGACGTTCCTCTGATATAGTTAC']

strings = [S0, S1, S2, S3, S4, S5, S6]

#fill table with LCS
def create_LCS_table(strings):
    n = len(strings)
    strings_col = strings[:]
    strings_row = strings[:]
    #initialize table
    table = [[0 for _ in range(n)] for _ in range(n)]
    for si in strings_col:
        for sj in strings_row:
            m = len(si[1])
            n = len(sj[1])
            table[si[0]][sj[0]] = LCS_length(si[1],sj[1])[m-1][n-1]
    return table

print('Table')
for row in create_LCS_table(strings):
    print(row)

def color_edges(strings,table):
    n = len(strings)
    edges_colors = [['None' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(strings[i][1]) - table[i][j] <= 20 and len(strings[j][1]) - table[i][j] <= 20:
                edges_colors[i][j] = 'Red'
            else:
                edges_colors[i][j] = 'Blue'
    return edges_colors

print(' ')
print('Colors edges')
for row in color_edges(strings,create_LCS_table(strings)):
    print(row)
