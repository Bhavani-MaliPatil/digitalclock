import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe - Colorful Edition")
        root.config(bg="#2C3E50")  # Dark blue background

        self.current = "X"
        self.board = [""] * 9
        self.buttons = []
        self.scores = {"X": 0, "O": 0}
        self.vs_computer = False

        self.colors = {
            "bg": "#2C3E50",       # Dark blue
            "board_bg": "#34495E", # Gray-blue
            "x_color": "#E74C3C",  # Red
            "o_color": "#3498DB",  # Blue
            "win_bg": "#2ECC71",   # Green
            "hover_bg": "#F1C40F"  # Yellow
        }

        self.build_ui()

    def build_ui(self):
        # Scoreboard
        self.score_label = tk.Label(
            self.root,
            text=self.get_score_text(),
            font=("Helvetica", 16, "bold"),
            bg=self.colors["bg"],
            fg="white"
        )
        self.score_label.pack(pady=5)

        # Turn label
        self.turn_label = tk.Label(
            self.root,
            text=f"Player {self.current}'s Turn",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["bg"],
            fg=self.colors["x_color"]
        )
        self.turn_label.pack(pady=5)

        # Game board frame
        frame = tk.Frame(self.root, bg=self.colors["board_bg"], padx=10, pady=10)
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame,
                text="",
                font=("Helvetica", 28, "bold"),
                width=4,
                height=2,
                bg=self.colors["board_bg"],
                fg="white",
                activebackground=self.colors["hover_bg"],
                relief="ridge",
                bd=4,
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.colors["hover_bg"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.colors["board_bg"]))
            self.buttons.append(btn)

        # Control buttons
        control_frame = tk.Frame(self.root, bg=self.colors["bg"])
        control_frame.pack(pady=8)

        reset = tk.Button(
            control_frame,
            text="🔄 Reset Game",
            font=("Helvetica", 12, "bold"),
            command=self.reset,
            bg="#F39C12",
            fg="white"
        )
        reset.grid(row=0, column=0, padx=5)

        toggle_ai = tk.Button(
            control_frame,
            text="🤖 Toggle AI",
            font=("Helvetica", 12, "bold"),
            command=self.toggle_ai,
            bg="#8E44AD",
            fg="white"
        )
        toggle_ai.grid(row=0, column=1, padx=5)

    def get_score_text(self):
        return f"Score - X: {self.scores['X']}  |  O: {self.scores['O']}"

    def toggle_ai(self):
        self.vs_computer = not self.vs_computer
        mode = "ON" if self.vs_computer else "OFF"
        messagebox.showinfo("Mode", f"Computer Mode: {mode}")

    def on_click(self, i):
        if self.board[i] == "":
            self.make_move(i)
            winner = self.check_winner()
            if winner:
                self.end_game(winner)
                return
            if self.vs_computer and self.current == "O":
                self.root.after(500, self.computer_move)

    def make_move(self, i):
        color = self.colors["x_color"] if self.current == "X" else self.colors["o_color"]
        symbol = "❌" if self.current == "X" else "⭕"
        self.board[i] = self.current
        self.buttons[i].config(text=symbol, fg=color, state="disabled")
        self.current = "O" if self.current == "X" else "X"
        self.turn_label.config(
            text=f"Player {self.current}'s Turn",
            fg=self.colors["o_color"] if self.current == "O" else self.colors["x_color"]
        )

    def computer_move(self):
        empty_cells = [i for i, v in enumerate(self.board) if v == ""]
        if empty_cells:
            choice = random.choice(empty_cells)
            self.make_move(choice)
            winner = self.check_winner()
            if winner:
                self.end_game(winner)

    def check_winner(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.highlight_winner(a, b, c)
                return self.board[a]
        if all(cell != "" for cell in self.board):
            return "Draw"
        return None

    def highlight_winner(self, a, b, c):
        for idx in (a, b, c):
            self.buttons[idx].config(bg=self.colors["win_bg"])

    def end_game(self, winner):
        if winner != "Draw":
            messagebox.showinfo("Result", f"🎉 Player {winner} wins!")
            self.scores[winner] += 1
        else:
            messagebox.showinfo("Result", "🤝 It's a draw!")
        self.score_label.config(text=self.get_score_text())
        self.disable_all()

    def disable_all(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset(self):
        self.current = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", state="normal", bg=self.colors["board_bg"])
        self.turn_label.config(
            text=f"Player {self.current}'s Turn",
            fg=self.colors["x_color"]
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
