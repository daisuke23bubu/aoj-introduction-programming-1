'''
n×m の行列 A と m×l の行列 B を入力し、それらの積である n×l の行列 C を出力するプログラムを作成してください。
'''
n,m,l =map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(m)]

c = [[0 for _ in range(l)]for _ in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    print(*c[i])
