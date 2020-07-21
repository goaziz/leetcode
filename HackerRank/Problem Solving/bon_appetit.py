def bonAppetit(bill, k, b):
    su = sum(bill) - bill[k]

    if (su // 2) == b:
        print('Bon Appetit')
    else:
        print(b - (su // 2))


bill = [3, 10, 2, 9]
k = 1
b = 7

bonAppetit(bill, k, b)
