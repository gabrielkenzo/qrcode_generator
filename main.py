# class Qrcode:
#     def __init__(self, size):
#         self.size = size
#         self.qrcode = self.build_matrix()

#     def build_matrix(self):
#         return [[0 for j in range(self.size)] for i in range(self.size)]

#     def __str__(self):
#         string = ""
#         for row in self.qrcode:
#             string = string + str(row) + "\n"
#         return string


# qrcode = Qrcode(3)
# print(qrcode)


# def is_valid(qrcode):
#     return True


# n = 3

# total_squares = n**2 - (n - 2) ** 2

# amount = 0
# for n_of_black_squares in range((total_squares // 2) + 1):
#     print(f"Total number of painted squares: {n_of_black_squares}")
#     possibilities = []
#     last_amount = 0
#     for k in range(total_squares):
#         while True:
#             # TODO(optimization): clean instead of regenerate qrcode
#             qrcode = [[0 for j in range(n - 1)] for i in range(4)]

#             # TODO: how can I generate every possible configuration given the number of black squares

#             if is_valid(qrcode):
#                 possibilities.append(qrcode)
#                 last_amount += 1
#     amount += last_amount
#     print(possibilities)
#     print()
# print(f"TOTAL AMOUNT: {amount*2 - last_amount}")



class QrCode:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def is_valid(self):
        if self.a == self.c and self.b == self.d:
            return False
        return True

n = 4

count = 0
possibilities = []
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                qrcode = QrCode(a, b, c, d)
                if qrcode.is_valid():
                    count += 1
                    possibilities.append([qrcode.a, qrcode.b, qrcode.c, qrcode.d])
print(count/4)
print(len(possibilities))




def is_permutation(list_1,list_2):
    if len(list_1) != len(list_2):
        return False

    for index in range(len(list_2)):
        if list_1 == list_2[index:]+list_2[:index]:
            return True
    return False

count = 0
while len(possibilities) != 0:
    qrcode = possibilities.pop(0)
    # if qrcode.is_valid():
    count += 1
    index = 0
    perms = [qrcode] #garbage
    while index < len(possibilities):
        if is_permutation(qrcode, possibilities[index]):
            perm = possibilities.pop(index)
            perms.append(perm) #garbage
        else:
            index += 1
    print(count) #garbage
    for k in perms: #garbage
        print(k) #garbage
    print() #garbage

