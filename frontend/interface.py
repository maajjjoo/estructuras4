import tkinter as tk
from engine.transactionEngine import TicketTransactionEngine


class Interface:

    def __init__(self):

        self.engine = TicketTransactionEngine()
        self.simulation_running = False

        self.window = tk.Tk()
        self.window.title("Travis Scott Ticket System")
        self.window.geometry("1000x700")
        self.window.configure(bg="#0b0b0b")

        self.buildInterface()

        self.window.mainloop()

    def buildInterface(self):

        # HEADER
        header = tk.Frame(self.window, bg="#0b0b0b")
        header.pack(pady=20)

        title = tk.Label(
            header,
            text="TRAVIS SCOTT - UTOPIA WORLD TOUR",
            font=("Arial", 24, "bold"),
            fg="#ffffff",
            bg="#0b0b0b"
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="Concert Ticket Transaction Processing System",
            font=("Arial", 12),
            fg="#bbbbbb",
            bg="#0b0b0b"
        )
        subtitle.pack()

        # EVENT PANEL
        event_panel = tk.Frame(self.window, bg="#1a1a1a", padx=20, pady=15)
        event_panel.pack(pady=10)

        event_label = tk.Label(
            event_panel,
            text="Event: Travis Scott Live Concert",
            font=("Arial", 14),
            fg="white",
            bg="#1a1a1a"
        )
        event_label.pack()

        info_label = tk.Label(
            event_panel,
            text="High demand event — transactions arriving every 3 seconds",
            font=("Arial", 10),
            fg="#cccccc",
            bg="#1a1a1a"
        )
        info_label.pack()

        # BUTTON PANEL
        button_panel = tk.Frame(self.window, bg="#0b0b0b")
        button_panel.pack(pady=15)

        self.simulation_button = tk.Button(
            button_panel,
            text="Start Purchase Simulation",
            font=("Arial", 11),
            width=24,
            height=2,
            bg="#6b0f1a",
            fg="white",
            activebackground="#8b1c2b",
            activeforeground="white",
            bd=0,
            command=self.startSimulation
        )
        self.simulation_button.grid(row=0, column=0, padx=20)

        process_button = tk.Button(
            button_panel,
            text="Process Next Transaction",
            font=("Arial", 11),
            width=24,
            height=2,
            bg="#6b0f1a",
            fg="white",
            activebackground="#8b1c2b",
            activeforeground="white",
            bd=0,
            command=self.processTransaction
        )
        process_button.grid(row=0, column=1, padx=20)

        # MAIN AREA
        main_frame = tk.Frame(self.window, bg="#0b0b0b")
        main_frame.pack(pady=20)

        # QUEUE PANEL
        queue_frame = tk.Frame(main_frame, bg="#1a1a1a", padx=15, pady=15)
        queue_frame.grid(row=0, column=0, padx=30)

        queue_title = tk.Label(
            queue_frame,
            text="Incoming Purchase Queue",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#1a1a1a"
        )
        queue_title.pack()

        self.queue_list = tk.Listbox(
            queue_frame,
            width=40,
            height=18,
            bg="#262626",
            fg="white",
            font=("Arial", 10),
            selectbackground="#8b1c2b",
            bd=0
        )
        self.queue_list.pack(pady=10)

        # FAILED PANEL
        failed_frame = tk.Frame(main_frame, bg="#1a1a1a", padx=15, pady=15)
        failed_frame.grid(row=0, column=1, padx=30)

        failed_title = tk.Label(
            failed_frame,
            text="Failed Transactions Log",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#1a1a1a"
        )
        failed_title.pack()

        self.failed_list = tk.Listbox(
            failed_frame,
            width=40,
            height=18,
            bg="#262626",
            fg="white",
            font=("Arial", 10),
            selectbackground="#8b1c2b",
            bd=0
        )
        self.failed_list.pack(pady=10)

        # STATUS
        status_panel = tk.Frame(self.window, bg="#0b0b0b")
        status_panel.pack(pady=15)

        self.status = tk.Label(
            status_panel,
            text="System Ready",
            font=("Arial", 12),
            fg="#dddddd",
            bg="#0b0b0b"
        )
        self.status.pack()

    def startSimulation(self):

        if not self.simulation_running:
            self.simulation_running = True
            self.status.config(text="Simulation started — incoming purchases enabled")
            self.simulatePurchase()

    def simulatePurchase(self):

        if self.simulation_running:

            self.engine.generatePurchaseRequest()

            self.updateQueue()

            self.window.after(3000, self.simulatePurchase)

    def processTransaction(self):

        result = self.engine.processTransaction()

        self.status.config(text=result)

        self.updateQueue()
        self.updateFailed()

    def updateQueue(self):

        self.queue_list.delete(0, tk.END)

        queue = self.engine.getQueue()

        for transaction in queue:
            self.queue_list.insert(tk.END, transaction)

    def updateFailed(self):

        self.failed_list.delete(0, tk.END)

        failed = self.engine.getFailedTransactions()

        for transaction in failed:
            self.failed_list.insert(tk.END, transaction)