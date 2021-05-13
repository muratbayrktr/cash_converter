#cash = input("Para miktarı:\t")
# 0 <= M <= 999.999.999.999 TL 
# 0 <= K <= 99 kuruş

ones = {
    0: "",
    1: "bir",
    2: "iki",
    3: "üç",
    4: "dört",
    5: "beş",
    6: "altı",
    7: "yedi",
    8: "sekiz",
    9: "dokuz",
}
 
tens = {
    0: "",
    1: "on",
    2: "yirmi",
    3: "otuz",
    4: "kırk",
    5: "elli",
    6: "altmış",
    7: "yetmiş",
    8: "seksen",
    9: "doksan",
}
hundreds = {
    0: "",
    1: "yüz",
    2: "ikiyüz",
    3: "üçyüz",
    4: "dörtyüz",
    5: "beşyüz",
    6: "altıyüz",
    7: "yediyüz",
    8: "sekizyüz",
    9: "dokuzyüz",
}


def receive_cash():
    inp = input("Please enter the cash in the form of \n[ 000.000.000.000,00 ]\n\nAmount:\t").split(",")
    while len(inp[0]) > 12 :
        print("Too big")
        inp = input("Please enter the cash in the form of \n[ 000.000.000.000,00 ]\n\nAmount:\t").split(",")
    return inp
def complete(string):
    length = len(string)
    tam = (12-length) // 3
    kalan = (12-length) % 3
    for t in range(tam):
        string = 3*"0" + string
    return kalan*"0" + string

def complete_kurus(string):
    length = len(string)
    return string + "0"*(2-length)


def convert_to_text(tam,kurus):
    global ones,tens,hundreds
    amount = complete("".join(tam.split(".")))
    kurus = complete_kurus(kurus[:20])
    if int(amount) == 0: result = "sıfır TL "
    else:
        milyar = 0 if int(amount[:3]) == 0 else 1
        milyon = 0 if int(amount[3:6]) == 0 else 1
        binn = 0 if int(amount[6:9]) == 0 else 1
        result = hundreds[int(amount[0])] + tens[int(amount[1])] + ones[int(amount[2])] + "milyar "*milyar \
               + hundreds[int(amount[3])] + tens[int(amount[4])] + ones[int(amount[5])] + "milyon "*milyon 
        if amount[6:9] == "001": result += "bin "
        else: result += hundreds[int(amount[6])] + tens[int(amount[7])] + ones[int(amount[8])] + "bin "*binn
        result += hundreds[int(amount[9])] + tens[int(amount[10])] + ones[int(amount[11])] + " TL "
    #kurus  
    k = 0 if int(kurus) == 0 else 1
    result += tens[int(kurus[0])] + ones[int(kurus[1])] + " kuruş"*k 
    return str.upper(result)

def main(money):
    print(convert_to_text(money[0],money[1]))

if __name__ == "__main__":
    cash = receive_cash()
    main(cash)
