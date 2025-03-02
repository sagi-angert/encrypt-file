from urllib.parse import to_bytes

hex_letters = ["a", "b", "c", "d", "e", "f"]

def convert_to_bin(hex): #converts a hex number to a binary one
    bin = ""
    hex = str(hex)
    for letter in hex:
        if letter in hex_letters:
            bin += convert_dec(10 + hex_letters.index(letter))
        else:
            bin += convert_dec(int(letter))
    bin = remove_start(bin)
    bin = fill_zero_8bits(bin)
    return bin

def remove_start(bin):  #removes all zeros at the start of a binary number
    while bin[0] == "0":
        bin = bin[1:]
    return bin

def remove_start_8bits(bin):   #removes all zeros at the start of a binary number until its length is at least 8 bits
    i = len(bin)
    while i > 8 and bin[0] == "0":
        bin = bin[1:]
        i -= 1
    return bin

def fill_zero_8bits(bin):   #adds zeros at the start of binary numbers until its 8 bits
    i = len(bin)
    bin = bin[::-1]
    while i < 8:
        bin += "0"
        i += 1
    bin = bin[::-1]
    return bin

def convert_dec(num):
    i = 128
    bin = ""
    while i >= 1:
        if (num - i >= 0):
            bin += "1"
            num -= i
        else:
            bin += "0"
        i /= 2
    bin = remove_start_8bits(bin)
    bin = fill_zero_8bits(bin)
    return bin

def xor(bin1, bin2):
    xorred = ""
    i = 0
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]
    while i < len(bin1) and i < len(bin2):
        if bin1[i] == bin2[i]:
            xorred  += "0"
        else:
            xorred += "1"
        i += 1
    while i < len(bin1):
        xorred += bin1[i]
        i += 1
    while i < len(bin2):
        xorred += bin2[i]
        i += 1
    xorred = remove_start_8bits(xorred)
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]
    xorred = xorred[::-1]
    return xorred

decrypt = 0
xor_num = convert_dec(int(input("enter a number to encrypt the file using xor command: ")))  # xorring each byte we have depending on input
xor_num = remove_start(xor_num)
while decrypt != 1:
    file = open("C:\\Users\\anger\\Downloads\\text.txt", "rb")
    file_data = file.read()
    byte_list = []
    for byte in file_data:
       byte_list.append(convert_dec(byte))
    for byte in range(len(byte_list)):
       byte_list[byte] = xor(byte_list[byte], xor_num)
    file.close()
    file = open("C:\\Users\\anger\\Downloads\\text.txt", "wb")
    file.truncate(0)
    for byte in range(len(byte_list)):
        byte_list[byte] = int(byte_list[byte], 2).to_bytes(1, "big")
        file.write(byte_list[byte])
    file.flush()
    decrypt = int(input("file encrypted. press 1 to exit or any other button to decrypt "))
    file.close()