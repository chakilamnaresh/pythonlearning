class InSufficientFundsError(Exception):
    pass

bal=100000
amount=float(input("enter amount"))
if(bal<amount):
    try:
        raise InSufficientFundsError
    except(InSufficientFundsError):
        print("balance is not sufficient")
    finally:
        print("bye")
else:
    print("transaction success")
