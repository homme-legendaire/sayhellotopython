A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(f'A: {sum(A)/3:.1f}')
print(f'B: {sum(B)/3:.1f}')
A_award = ''
B_award = ''
if A[0] >= 90:
    A_award += ' Korean'
if A[1] >= 90:
    A_award += ' Math'
if A[2] >= 90:
    A_award += ' English'
if B[0] >= 90:
    B_award += ' Korean'
if B[1] >= 90:
    B_award += ' Math'
if B[2] >= 90:
    B_award += ' English'
print(f'A awards:{A_award}')
print(f'B awards:{B_award}')
