def makeData(line: str):
    s = line.split(',')
    
    date = ''
    time = 0
    price = 0
    
    date = int(s[1])
    time = int(s[2])
    price = float(s[3])
    
    return date, time, price

data = [0, 0.0]

flag_for_sale = False
i_sale = 0
mass_for_sale = [0.0]

flag_for_buy = True
i_buy = 0
mass_for_buy = [20000.0]

capital = int(input("Введите стартовй бюджет: "))
tr_limit = int(input("Введите число возможных транзакций: "))

with open("new.csv", "r") as f:
    for line in f.readlines():
        line = line[:-1]
        if line == ',date,time,price':
            continue
        else:
            date, time, price = makeData(line)

        if price > mass_for_sale[i_sale]:
            mass_for_sale.append(price)
            i_sale += 1

        elif price < mass_for_buy[i_buy]:
            mass_for_buy.append(price)
            i_buy += 1
        

        if len(mass_for_sale) == 4:
            flag_for_sale = True
            mass_for_sale = [0.0]
            i_sale = 0

        if (data[0] != 0) and flag_for_sale:            
            print('- '*15)
            print('Продаем', data[0], 'акций по цене', price)
            print('Дата продажи:', date, '\nВремя продажи:', time)
            capital += data[0] * price
            print('Остаток на счете:', capital)
            print('- '*15)

            data[0] = 0
            data[1] = 0.0
            flag_for_sale = False
            tr_limit -= 1

        if len(mass_for_buy) == 4:
            flag_for_buy = True
            mass_for_buy = [20000.0]
            i_buy = 0

        if (data[0] == 0) and flag_for_buy and capital > price:
            print('- '*15)
            data[0] = int(capital / (price * 2))
            data[1] = price
            print('Покупаем', data[0], 'акций по цене', data[1])
            print('Дата покупки:', date, '\nВремя покупки:', time)
            capital -= data[0] * data[1]
            print('Остаток на счете:', capital)
            print('- '*15)
            flag_for_buy = False

        if tr_limit == 0:
            break

if data[0] > 0:
    print('- '*10)
    print('Продаем', data[0], 'акций по цене', price)
    print('Дата продажи:', date, '\nВремя продажи:', time)
    capital += data[0] * price
    print('Остаток на счете:', capital)
    print('- '*10)

