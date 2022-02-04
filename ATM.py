class Atm(object):
    def __init__(self, cardNumber, pinNumber, company):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.company = company
        pass

    def cashWithdrawl(self):
        print("$200 has been withdrawled from your account")

    def balanceEnquiry(self):
        print("Account balance: $5000")

    def bankTransfer(self):
        print("$10,000 has been transfered into your account")

backAccount = Atm("3498 2771 3672 4333", "3256", "ANZ")
print(backAccount.balanceEnquiry())