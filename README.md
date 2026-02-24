Candidate is requested to implement the reconciliation process with ETL steps as follows:
1. Extract invoice data from a CSV file
2. Extract bank transaction data from a mock API endpoint
4. Transform and automatically reconcile the data to match invoices with corresponding transactions based on amount and date
5. Load the reconciliation results into a Django model for further manual reconciliation and reporting

Notes:
- The implementation should be scalable to handle larger datasets (e.g., >100k records)