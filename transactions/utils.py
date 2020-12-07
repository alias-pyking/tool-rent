from .models import Transaction


def get_transaction_or_none(transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        transaction = None
    return transaction
