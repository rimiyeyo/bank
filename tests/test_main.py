import io

import pytest
from unittest.mock import patch

from main import Account


@pytest.mark.parametrize(
    "balance, deposit_money",
    [
        (1000000, 0),
        (1000000, -1),
    ],
)
def test_deposit_negative_or_zero_raises(balance: int, deposit_money: int) -> None:
    account = Account(balance)
    with pytest.raises(AssertionError, match="입금액은 0원이상 입금할 수 있습니다."):
        account.deposit(deposit_money)


@pytest.mark.parametrize(
    "balance, transfer_money",
    [
        (1000000, 0),
        (1000000, -1),
    ],
)
def test_transfer_negative_or_zero_raises(balance: int, transfer_money: int) -> None:
    account = Account(balance)
    with pytest.raises(
        AssertionError, match="출금액은 0원 초과 금액부터 출금할 수 있습니다."
    ):
        account.transfer(transfer_money)


@pytest.mark.parametrize(
    "balance, transfer_money",
    [
        (1, 1000),
        (1000, 1001),
    ],
)
def test_transfer_raises_value_error(balance: int, transfer_money: int) -> None:
    account = Account(balance)
    with pytest.raises(AssertionError, match="계좌에 인출할 충분한 잔액이 없습니다."):
        account.transfer(transfer_money)


@pytest.mark.parametrize(
    "balance, transfer_money",
    [
        (-1, 1000),
        (0, 1000),
    ],
)
def test_balance_zero_raise(balance: int, transfer_money: int) -> None:
    account = Account(balance)
    with pytest.raises(AssertionError, match="계좌에 잔액이 0원미만 입니다."):
        account.transfer(transfer_money)


@pytest.mark.parametrize(
    "balance, transfer_money, expected",
    [
        (1500, 1000, 500),
        (1500, 1500, 0),
    ],
)
def test_transfer_success(balance: int, transfer_money: int, expected: int) -> None:
    account = Account(balance)
    new_balance = account.transfer(transfer_money)
    assert new_balance == expected


@pytest.mark.parametrize(
    "balance, transfer_money",
    [
        (1500, 1000),
    ],
)
def test_transfer_success_stdout_patch(balance: int, transfer_money: int) -> None:
    account = Account(balance)
    with patch("sys.stdout", new=io.StringIO()) as fake_out:
        account.transfer(transfer_money)
        output = fake_out.getvalue()
    assert "계좌에서 돈이 출금되었습니다. 출금 후 잔액은 500원 입니다.\n" == output
