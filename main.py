class Qrcode:
    def __init__(self, size):
        self.size = size
        self.qrcode = self.build_matrix()

    def build_matrix(self):
        return [[0 for j in range(self.size)] for i in range(self.size)]

    def __str__(self):
        string = ""
        for row in self.qrcode:
            string = string + str(row) + "\n"
        return string


# qrcode = Qrcode(3)
# print(qrcode)


def is_valid(qrcode):
    return True


n = 3

total_squares = n**2 - (n - 2) ** 2

amount = 0
for n_of_black_squares in range((total_squares // 2) + 1):
    print(f"Total number of painted squares: {n_of_black_squares}")
    possibilities = []
    last_amount = 0
    for k in range(total_squares):
        while True:
            # TODO(optimization): clean instead of regenerate qrcode
            qrcode = [[0 for j in range(n - 1)] for i in range(4)]

            # TODO: how can I generate every possible configuration given the number of black squares

            if is_valid(qrcode):
                possibilities.append(qrcode)
                last_amount += 1
    amount += last_amount
    print(possibilities)
    print()
print(f"TOTAL AMOUNT: {amount*2 - last_amount}")
