import csv

from external_resources.invoice_data import INVOICE_DATA_CSV_PATH
from external_resources.mock_bank_api import MockBankAPIServer
from external_resources.reconciliation_report import ReconciliationReport
from external_resources.secrets import MOCK_BANK_API_TOKENS

csv_path = INVOICE_DATA_CSV_PATH
tokens = MOCK_BANK_API_TOKENS
api = MockBankAPIServer()

request = {
    "Headers": {
        "auth_token": next(iter(tokens))
    }
}


def get_transactions():
    MAX_RETRIES = 5
    status_code = 500
    while status_code == 500:
        transactions = api.get_transactions(request)
        status_code = transactions.status_code
        MAX_RETRIES -= 1
        if MAX_RETRIES == 0 and status_code != 200:
            raise Exception("Max retries reached")
        # [{'id': '001', 'amount': 50.0, 'date': '2024-07-10', 'note': 'Payment for INV-001'},
        # {'id': '002', 'amount': 200.0, 'date': '2024-07-15', 'note': 'Payment for INV-002'}]
    transactions_data = transactions.json()
    refined_transactions_dict = {}
    transactions_dict = {d["id"]: d for d in transactions_data}

    for transaction in transactions_data:
        refined_transactions_dict[transaction["note"]] = {
            "amount": transaction["amount"],
            "date": transaction["date"],
            "id": transaction["id"],
        }
    return refined_transactions_dict, transactions_dict


def get_invoices():
    invoices = {}
    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if len(row) == 3:
                invoices[row[0]] = {
                    "amount": row[1],
                    "date": row[2],
                }
    return invoices


# [{'invoice_id': 'INV-001', 'amount': '100.00', 'date': '2024-07-01'},
# {'invoice_id': 'INV-002', 'amount': '200.00', 'date': '2024-07-15'}]

# for invoice_id in invoices.keys():
#     for transaction_note in refined_transactions_dict.keys():
#         transaction_id = refined_transactions_dict[transaction_note]["id"]
#         if invoice_id in transaction_note:
#             if invoice_id not in reconciled:
#                 reconciled.append(invoice_id)
#                 break
#             else:
#                 if invoice_id not in unmatched_invoices:
#                     unmatched_invoices.append(invoice_id)
#         else:
#             if transaction_id not in unmatched_transactions:
#                 unmatched_transactions.append(transaction_id)

def generate_report(refined_transactions_dict, invoices):
    reconciled = []
    unmatched_transactions = []

    for transaction_note in refined_transactions_dict.keys():
        invoice_id = transaction_note.replace("Payment for ", "")
        invoice = invoices.get(invoice_id)
        if invoice:
            reconciled.append(invoice_id)
            del invoices[invoice_id]
        else:
            transaction_id = refined_transactions_dict[transaction_note]["id"]
            unmatched_transactions.append(transaction_id)

    unmatched_invoices = [l for l in invoices.keys()]
    report = ReconciliationReport(reconciled, unmatched_invoices, unmatched_transactions)
    return report


# BONUS PART

def generate_bonus_csv(unmatched_transactions, unmatched_invoices, transactions_dict, invoices):
    bonus_csv = "bonus.csv"
    bonus_csv_headers = ["ID", "type", "metadata"]
    bonus_csv_data = []

    for unmatched_transaction in unmatched_transactions:
        bonus_csv_data.append([unmatched_transaction, "transaction", transactions_dict[unmatched_transaction]])
    for unmatched_invoice in unmatched_invoices:
        bonus_csv_data.append([unmatched_invoice, "invoice", invoices[unmatched_invoice]])

    with open(bonus_csv, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(bonus_csv_headers)
        writer.writerows(bonus_csv_data)


if __name__ == "__main__":
    refined_transactions_dict, transactions_dict = get_transactions()
    invoices = get_invoices()
    report = generate_report(refined_transactions_dict, invoices)
    report.print_report()
    generate_bonus_csv(report.unmatched_transactions, report.unmatched_invoices, transactions_dict, invoices)
