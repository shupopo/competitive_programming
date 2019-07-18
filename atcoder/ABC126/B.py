S = list(input())
former = 0
latter = 0

if int(S[0]) == 0:
    former = int(S[1])
else:
    former = int(S[0]+S[1])


if int(S[2]) == 0:
    latter = int(S[3])
else:
    latter = int(S[2] + S[3])


if former == 0 or latter == 0:
    if former == 0 and latter == 0:
        print('NA')
    elif former == 0 and latter < 13:
        print('YYMM')
    elif former < 13 and latter == 0:
        print('MMYY')
    else:
        print('NA')
else:
    if former > 12 and latter > 12:
        print('NA')
    elif former > 12 and latter < 13:
        print('YYMM')
    elif former < 13 and latter > 12:
        print('MMYY')
    elif former < 13 and latter < 13:
        print('AMBIGUOUS')
