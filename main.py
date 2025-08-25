class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, deposit_money: int) -> int:
        assert deposit_money > 0, "입금액은 1원 이상부터 입금할 수 있습니다."
        self.balance += deposit_money
        print(f"입금이 되었습니다. 입금 후 잔액은 {self.balance}원 입니다.")
        return self.balance

    def transfer(self, transfer_money: int) -> int:
        assert self.balance > 0, "계좌에 잔액이 0원이하 입니다."
        assert transfer_money > 0, "출금액은 1원 이상부터 출금할 수 있습니다."
        assert self.balance >= transfer_money, "계좌에 인출할 충분한 잔액이 없습니다."
        self.balance -= transfer_money
        print(f"계좌에서 돈이 출금되었습니다. 출금 후 잔액은 {self.balance}원 입니다.")
        return self.balance


if __name__ == "__main__":
    account = Account()
    account.deposit(1000)
    account.transfer(1000)
