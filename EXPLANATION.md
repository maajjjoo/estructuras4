# System Design Explanation

## Relationship with the Banking Transaction Case Study

The original case study describes a **banking transaction engine** used to process financial operations in real time.

In this project, the same concept was adapted to a **concert ticket purchasing system**. Each ticket purchase is treated as a transaction that must be processed by the system.

Although the context is different, the internal logic follows the same principles used in financial systems.

---

## Queue Implementation

The queue is used to manage incoming purchase requests.

In a real online ticket platform, multiple users may attempt to buy tickets at the same time.
If the server cannot process all requests immediately, they are stored in a queue to avoid losing any transactions.

The queue follows the **FIFO principle (First In, First Out)**.

This means that the first purchase request received is the first one to be processed.

Example:

```
Customer 101 - 2 tickets
Customer 102 - 1 ticket
Customer 103 - 3 tickets
```

The system processes them in that same order.

---

## Stack Implementation

The stack is used during transaction processing to manage rollback operations.

Each transaction consists of several internal steps:

1. Reserve seats
2. Validate payment
3. Confirm purchase

These steps are stored in a stack.
If an error occurs during the process, the system uses the stack to reverse the operations in the opposite order.

Example rollback sequence:

```
Undo confirm purchase
Undo validate payment
Undo reserve seats
```

This follows the **LIFO principle (Last In, First Out)**.

---

## Array Implementation

The system stores recent failed transactions in a fixed-size array.

This array acts as a simple auditing mechanism that allows the system to keep track of recent transaction failures without consuming excessive memory.

Only the most recent failures are kept.

Example:

```
Customer 205 - 3 tickets
Customer 310 - 1 ticket
Customer 412 - 2 tickets
```

If the array reaches its maximum capacity, the oldest record is removed to make space for the new one.

---

## Simulation of High Demand

To simulate a real ticket purchasing scenario, the system automatically generates purchase requests every **3 seconds**.

Each request contains a random number of tickets between **1 and 3**.

There is also a **40% probability of transaction failure** to represent situations such as payment errors or server overload during high-demand events.

---

## Conclusion

This system demonstrates how basic data structures can be applied to model real-world transaction processing systems.

Even though the scenario is based on a concert ticket platform, the same architecture can be applied to banking systems, payment gateways, or any application that requires reliable transaction management.
