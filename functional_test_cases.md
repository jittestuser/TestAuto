# Functional Test Cases for Banking Application

## 1. User Login
- Verify that a registered user can log in with valid credentials.
- Verify that login fails with invalid credentials.
- Verify that the system locks the account after multiple failed login attempts.
- Verify that password reset functionality works as expected.

## 2. Account Management
- Verify that users can view their account details (balance, account number, etc.).
- Verify that users can update their personal information.
- Verify that changes to personal information are reflected immediately.

## 3. Fund Transfer
- Verify that users can transfer funds between their own accounts.
- Verify that users can transfer funds to other users’ accounts.
- Verify that the system validates sufficient balance before allowing a transfer.
- Verify that a confirmation message is displayed after a successful transfer.
- Verify that failed transfers (e.g., due to insufficient funds) show appropriate error messages.

## 4. Transaction History
- Verify that users can view their transaction history.
- Verify that transaction history displays correct details (date, amount, type).
- Verify that users can filter transactions by date range.

## 5. Bill Payment
- Verify that users can pay bills using their account.
- Verify that bill payment is reflected in the transaction history.
- Verify that failed bill payments show appropriate error messages.

## 6. Logout
- Verify that users can log out successfully.
- Verify that session is terminated after logout and user cannot access account without logging in again.

## 7. Security
- Verify that sensitive information is not displayed in plain text.
- Verify that session times out after a period of inactivity.
