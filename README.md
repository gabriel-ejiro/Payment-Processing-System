# Payment-Processing-System

                                                          Payment Processing System
🎯 Objective

The goal of this task is to design a flexible payment system that can dynamically switch between different payment methods (e.g., credit card, PayPal, cryptocurrency) at runtime. You will implement the Strategy Pattern to encapsulate different payment algorithms and make the system easily extendable.

📘 Domain Story

A digital e-commerce platform wants to allow customers to choose how they want to pay for their order. The platform should support different payment methods and allow adding new ones (like Apple Pay or bank transfer) without modifying the core order logic.
The company expects flexibility and reusability in the codebase — ideal for the Strategy Pattern.

📋 Requirements

Implement a PaymentStrategy interface with a method pay(amount).

Implement at least three payment strategies:

            -  Credit Card
            -  PayPal
            -   Cryptocurrency

Allow switching between strategies at runtime.

Create a PaymentContext class that uses the selected strategy to execute the payment.

Provide a simple CLI simulation of user selecting a method and making a payment.

🧱 Class Structure
PaymentStrategy:	Strategy interface
CreditCardPayment:	Concrete strategy
PayPalPayment:	Concrete strategy
CryptoPayment:	Concrete strategy
PaymentContext:	Context that uses a payment strategy


Possible Extensions (Advanced)

Add more strategies (e.g., Apple Pay, Bank Transfer).

Store and validate user payment data for each method.
Implement a simple GUI or web interface.

Log payment transactions into a JSON or database.

