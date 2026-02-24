from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class ReconciliationReport:
    reconciled: list[object]
    unmatched_invoices: list[object]
    unmatched_transactions: list[object]

    def print_report(self):
        print("\n" + "=" * 30)
        print("Reconciliation Report:")

        print(f"Total Reconciled: {len(self.reconciled)}")

        print(f"Unmatched Invoices: {len(self.unmatched_invoices)}")
        for idx, invoice in enumerate(self.unmatched_invoices, start=1):
            print(f"{idx} - unmatched Invoice: '{invoice}'")

        print(f"Unmatched Transactions: {len(self.unmatched_transactions)}")
        for idx, transaction in enumerate(self.unmatched_transactions, start=1):
            print(f"{idx} - unmatched Transaction: '{transaction}'")

        print("=" * 30 + "\n")


class BaseReconciliationService(ABC):
    @abstractmethod
    def get_reconciliation_report(self) -> ReconciliationReport:
        ...
