

upc = '03600024145'

upc_length = len(upc)

print("Current UPC (without check digit): " + upc + "  ->  Len: " + str(upc_length))

if upc_length == 11:
    print("Calculating check digit for length 12")
    upc_reversed = []
    for i in range(1, upc_length):
        upc_reversed.append(upc[i*(-1)])
    upc_reversed.append(upc[0])
    #print(str(upc_reversed))

    even_digits = []
    odd_digits = []
    for i in range(0, upc_length):
        if i % 2 == 0: #switched even and off due to position count starting from 1
            odd_digits.append(upc_reversed[i])
        else:
            even_digits.append(upc_reversed[i])
    #print(str(odd_digits))
    #print(str(even_digits))

    odd_product = 0
    for i in odd_digits:
        odd_product = odd_product + int(i)

    odd_product = odd_product * 3

    even_sum = 0
    for i in even_digits:
        even_sum = even_sum + int(i)

    combined_sum = odd_product + even_sum

    check_digit = 10 - (combined_sum % 10)

    print("Calculated check digit : " + str(check_digit))
    print("Combined UPC : " + upc + str(check_digit))