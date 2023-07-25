#include <iostream>
#include <string>
#include <vector>

class BankAccount {
private:
    std::string accountNumber;
    std::string accountHolder;
    double balance;

public:
    BankAccount(std::string accNumber, std::string accHolder)
        : accountNumber(accNumber), accountHolder(accHolder), balance(0) {}

    void deposit(double amount) {
        balance += amount;
    }

    bool withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }

    double getBalance() const {
        return balance;
    }

    std::string getAccountHolder() const {
        return accountHolder;
    }

    std::string getAccountNumber() const {
        return accountNumber;
    }
};

class Bank {
private:
    std::vector<BankAccount> accounts;

public:
    void createAccount(std::string accNumber, std::string accHolder) {
        accounts.push_back(BankAccount(accNumber, accHolder));
    }

    BankAccount* findAccount(const std::string& accNumber) {
        for (auto& account : accounts) {
            if (account.getAccountNumber() == accNumber) {
                return &account;
            }
        }
        return nullptr;
    }

    bool makeDeposit(std::string accNumber, double amount) {
        BankAccount* account = findAccount(accNumber);
        if (account) {
            account->deposit(amount);
            return true;
        }
        return false;
    }

    bool makeWithdrawal(std::string accNumber, double amount) {
        BankAccount* account = findAccount(accNumber);
        if (account) {
            return account->withdraw(amount);
        }
        return false;
    }

    void printAccountInfo(std::string accNumber) {
        BankAccount* account = findAccount(accNumber);
        if (account) {
            std::cout << "Account Number: " << account->getAccountNumber() << std::endl;
            std::cout << "Account Holder: " << account->getAccountHolder() << std::endl;
            std::cout << "Balance: " << account->getBalance() << std::endl;
        } else {
            std::cout << "Account not found." << std::endl;
        }
    }
};

int main() {
    Bank bank;

    // Example usage:
    bank.createAccount("123456", "Frey");
    bank.createAccount("789012", "Nishant");

    bank.makeDeposit("123456", 1000);
    bank.makeWithdrawal("789012", 500);

    bank.printAccountInfo("123456");
    bank.printAccountInfo("789012");

    return 0;
}

