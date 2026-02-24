from dataclasses import dataclass
from typing import Optional
from io import StringIO
import random

"""
Candidate is requested to implement the reconciliation process with ETL steps as follows:
1. Extract invoice data from a CSV file
2. Extract bank transaction data from a mock API endpoint
4. Transform and automatically reconcile the data to match invoices with corresponding transactions based on amount and date
5. Load the reconciliation results into a Django model for further manual reconciliation and reporting

Notes:
- The implementation should be scalable to handle larger datasets (e.g., >100k records)
"""


def get_invoice_csv_data() -> StringIO:
    csv_data = """
    invoice_number,total_amount,due_date
    INV-001,100.00,2024-07-01
    INV-002,200.00,2024-07-15
    INV-003,150.00,2024-08-01
    INV-004,,2024-08-10
    INV-005,300.00,INVALID_DATE
    BROKEN_ROW
    """
    return StringIO(csv_data.strip())


@dataclass
class MockHttpResponse:
    status_code: int
    data: Optional[list[dict]] = None

    def json(self):
        return self.data


class MockBankAPIServer:
    """
    Authentication: Requires an "auth_token" in the request header. Valid token is "jtX6Qm^kU,%5]uCG".
    """

    def get_transactions(self, request: dict) -> MockHttpResponse:
        if random.random() < 0.5:
            return MockHttpResponse(status_code=500, data=None)
        if request.get("Headers", {}).get("auth_token") != "jtX6Qm^kU,%5]uCG":
            return MockHttpResponse(status_code=401, data=None)
        return MockHttpResponse(status_code=200, data=self._get_mock_transactions_data())

    @staticmethod
    def _get_mock_transactions_data() -> list[dict]:
        return [
            {"amount": 50.00, "date": "2024-07-10", "note": "Partial payment for INV-001"},
            {"amount": 200.00, "date": "2024-07-15", "note": "Payment for INV-002"},
            {"amount": 100.00, "date": "2024-07-20", "note": "Payment for INV-216"},
            {"amount": 150.00, "date": "2024-08-01", "note": "Payment for INV-003"},
        ]
