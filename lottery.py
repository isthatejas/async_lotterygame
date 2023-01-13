
import random
import tkinter as tk

class Lottery:
    def __init__(self, entry_fee):
        self.entry_fee = entry_fee
        self.current_number = None
        self.previous_number = None
    
    def start_lottery(self):
        self.current_number = random.randint(1, 100)
        self.previous_number = self.current_number
    
    def guess_higher_or_lower(self, guess):
        if self.entry_fee > 0:
            self.current_number = random.randint(1, 100)
            if (guess == "higher" and self.current_number > self.previous_number) or (guess == "lower" and self.current_number < self.previous_number):
                self.entry_fee = 0
                return "Congratulations, you have won the lottery!"
            else:
                self.entry_fee -= 1
                return "Sorry, your guess was incorrect. The correct number was: {}. You have {} tries left".format(self.current_number, self.entry_fee)
            self.previous_number = self.current_number
        else:
            return "Sorry, you have no more tries left. Please pay the entry fee to play again."

class LotteryApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.entry_fee = 3
        self.lottery = Lottery(self.entry_fee)
        self.lottery.start_lottery()
        
        self.title("Lottery Game")
        self.geometry("300x150")
        self.configure(bg='#a1dbcd')
        
        self.label = tk.Label(self, text="Current Number: {}".format(self.lottery.current_number),bg='#a1dbcd', fg='#383a39', font=("Helvetica", 14))
        self.label.pack()
        
        self.guess_var = tk.StringVar()
        self.guess_var.set("higher")
        
        self.guess_rb1 = tk.Radiobutton(self, text="Higher", variable=self.guess_var, value="higher",bg='#a1dbcd', fg='#383a39', font=("Helvetica", 14))
        self.guess_rb1.pack()
        
        self.guess_rb2 = tk.Radiobutton(self, text="Lower", variable=self.guess_var, value="lower",bg='#a1dbcd', fg='#383a39', font=("Helvetica", 14))
        self.guess_rb2.pack()
        
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_guess,bg='#383a39', fg='white', font=("Helvetica", 14))
        self.submit_button.pack()
        self.result_label = tk.Label(self, text="", bg='#a1dbcd', fg='#383a39', font=("Helvetica", 14))
        self.result_label.pack()
        
        self.pay_entry_fee_button = tk.Button(self, text="Pay Entry Fee", command=self.pay_entry_fee, bg='#383a39', fg='white', font=("Helvetica", 14))
        self.pay_entry_fee_button.pack()
        
    def submit_guess(self):
        guess = self.guess_var.get()
        result = self.lottery.guess_higher_or_lower(guess)
        self.result_label.config(text=result)
        
    def pay_entry_fee(self):
        self.entry_fee = 3
        self.lottery.start_lottery()
        self.label.config(text="Current Number: {}".format(self.lottery.current_number))
        self.result_label.config(text="")

if __name__ == "__main__":
    app = LotteryApp()
    app.mainloop()
