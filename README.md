# Travis Scott Ticket Transaction System

## Project Description

This project simulates a transaction processing system for an online ticket sales platform.
The scenario represents a high-demand concert event: **Travis Scott – Utopia World Tour**.

The system demonstrates how transaction management can be implemented using fundamental data structures such as **queues, stacks, and arrays**.

The application includes a graphical interface built with **Python and Tkinter**, where incoming purchase requests are simulated and processed as transactions.

---

## System Behavior

In a real ticket platform, thousands of users attempt to buy tickets simultaneously.
To manage this traffic, the system receives purchase requests and stores them in a **transaction queue**.

Each request is processed step by step. If an error occurs during processing, the system reverses the executed steps and records the failed transaction.

---

## Main Features

* Automatic simulation of incoming purchase requests every **3 seconds**
* Random ticket requests between **1 and 3 tickets**
* **40% probability of transaction failure** to simulate high system load
* Processing of transactions using queue logic
* Rollback mechanism using a stack
* Failed transaction logging using a fixed-size array
* Graphical user interface for interaction

---

## Technologies Used

* Python
* Tkinter (GUI)
* Object-Oriented Programming
* Data Structures (Queue, Stack, Array)

---

## Project Structure

```
estructuras4
│
├── engine
│   └── transactionEngine.py
│
├── frontend
│   └── interface.py
│
├── structures
│   ├── queue.py
│   ├── stack.py
│   └── failedTransactionsArray.py
│
└── main.py
```

---

## How to Run the Project

1. Open a terminal in the project folder.
2. Run the program:

```
python main.py
```

3. Click **Start Purchase Simulation** to generate incoming ticket requests.
4. Click **Process Next Transaction** to process each transaction.

---

## Educational Purpose

The goal of this project is to demonstrate how fundamental data structures can be applied to simulate real-world transaction systems, such as payment gateways or ticket purchasing platforms.
