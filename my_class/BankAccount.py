from random import randrange
from typing import List


class BankAccount:
    """
    Bank accunt mangement
    """
    all_account_numbers: List[int] = []
    last_account_number = 999

    def __init__(self, name: str) -> None:

        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number: int = an
        BankAccount.all_account_numbers.append(an)
        self.name = name
        self.balance: float = 0

    def display(self) -> None:

        """

        Show account balance.
        :return:
        """
        print(40 * "_")
        print(f"Hi,{self.name}\nYour current balance:{self.balance}")
        print(40 * "_")

    def deposit(self) -> None:
        """
        Increase account balance.
        :return:
        """
        amount = float(input("Please enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdrow(self) -> None:
        """
        withdrow from bank account
        :return:
        """
        amount = float(input("Enter amount to withdrow: "))
        if amount > self.balance:
            print("Insufficient Baleance!")
        else:
            self.balance -= amount
        self.display()


def main():
    # acc1 = BankAccount("Sajjad Sokhanvari")
    # print(40 * "*")
    # print(f"account_number:{acc1.account_number}")
    # print(40 * "*")
    # acc1.display()
    #
    # while True:
    #     choose = int(input("Enter:\n1 to see your balance,\n2 to diposit\n"
    #                        "3 to withdraw\n\t\t your chooise:  "))
    #     if choose == 1:
    #         acc1.display()
    #     elif choose == 2:
    #         acc1.deposit()
    #     elif choose == 3:
    #         acc1.withdrow()
    #     elif choose == 4:
    #         break
    #     else:
    #         print("your chooise is False! ")
    ac1=BankAccount("sajjad")
    print(BankAccount.all_account_numbers)
    ac2=BankAccount("ali")
    print(BankAccount.all_account_numbers)
    ac3=BankAccount("sara")
    print(BankAccount.all_account_numbers)


    print("account numner:",ac1.account_number)
    print("account numner:", ac2.account_number)
    print("account numner:", ac3.account_number)


if __name__ == "__main__":
    main()
