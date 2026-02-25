Candidate is requested to implement a reconciliation process with the following ETL steps:
1. Extract invoice data from a CSV file. The path to the CSV file is specified in `external_resources/invoice_data.py`.
2. Extract bank transaction data from a mock API endpoint. The API should be accessed via the `MockBankAPI` class defined in `external_resources/mock_bank_api.py`.
3. Produce a `ReconciliationReport` (defined in `external_resources/reconciliation_report.py`) by matching invoices with transactions based on criteria identified through data analysis.

Bonus points for:
- Generating a CSV report summarizing matched and unmatched records.

Notes:
- The implementation should be scalable to handle larger datasets (e.g., >100k records).
- Provide sufficient test coverage (unit and integration tests) to validate the reconciliation logic.
- Ensure proper error handling, enabling efficient debugging