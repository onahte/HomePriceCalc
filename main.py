''' Home prices have risen significantly during the past year due to low interest rates. This program calculates
    if it's worth paying the increased home price (=current) with the low interest or paying a lower home price
    (=original) with a higher interest rate.'''

def formatDollar(amount):
    amount = str(amount).split('.')
    dollar,change = amount[0],amount[1]
    for _ in range(len(dollar)-1,0,-1):
        if _ % 3 == 0:
            dollar = dollar[:len(dollar)-_] + ',' + dollar[len(dollar)-_:]
    if len(change) <= 1:
        change += '0'
    amount = dollar + '.' + change
    return amount


def main():
    original = int(input('Original Home Price: '))
    orig_int = float(input('Interest on original: '))/100
    current = int(input('Home Price after increase: '))
    incr_int = float(input('Interest on Home Price after increase: '))/100
    years = int(input('Years: '))
    orig_payable = original*orig_int*years + original
    incr_payable = current*incr_int*years + current

    if orig_payable > incr_payable:
        bigger = 'Original Home Price'
        diff = orig_payable - incr_payable
    else:
        bigger = 'Home Price after increase'
        diff = incr_payable - orig_payable

    print(f'Amount to be paid on Original Home Price: ${formatDollar(orig_payable)}' )
    print(f'Amount to be paid on Increased Home Price: ${formatDollar(incr_payable)}' )
    print(f'The {bigger} costs more by ${formatDollar(diff)}')

if __name__ == '__main__':
    main()