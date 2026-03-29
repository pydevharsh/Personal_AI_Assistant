import tkinter as tk

# window :
window = tk.Tk()
window.title("Personal Bot")
window.geometry("420x550")
window.config(bg="#0f172a")

# grid config
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# === TOP BAR ===
header_label = tk.Label(
    window, 
    text="Personal AI Assistant",
    bg="#1e293b", fg="#e2e8f0",
    font=("Times New Roman", 14, "bold"),
    pady=12
)
header_label.grid(row=0, column=0, sticky="ew")

# === CHAT AREA ===
chat_area = tk.Text(
    window,
    bg="#0f172a", 
    fg="white",
    font=("Courier", 10),
    pady=10,
    wrap="word")
chat_area.grid(row=1, column=0, sticky="nsew")
chat_area.config(state="disabled")

# === INPUT AREA ===
input_frame = tk.Frame(window, bg="#1e293b")
input_frame.grid(row=2, column=0, sticky="ew")

input_frame.columnconfigure(0, weight=1)

# === Responses Dictonary ===
# responses = {
#     "hi" : "Hello! How Can I Help You Today ?",
#     "hello" : "Hi There! How's It Going ?",
#     "how are you" : "I'm Just A Bot, Bot I'm Doing Great!",
#     "bye" : "Goodbye! Have A Nice Day!",
#     "help" : "Sure! I Can Chat With You.\nTry Saying (hi, hello, how are you, bye)"
# }

responses = {
    "hi": "Hello! How Can I Help You Today?",
    "hello": "Hi There! How's It Going?",
    "hey": "Hey! What's Up?",
    "how are you": "I'm Just A Bot, But I'm Doing Great! 😄",
    "what's up": "Not Much! How About You?",
    "how is life": "Life Is Digital And Full Of Zeros And Ones! 😎",
    "good morning": "Good Morning! Have A Fantastic Day Ahead!",
    "good afternoon": "Good Afternoon! How's Your Day Going?",
    "good evening": "Good Evening! Hope You Had A Great Day!",
    "good night": "Good Night! Sleep Well And Recharge! 🌙",
    "bye": "Goodbye! Have A Nice Day!",
    "see you": "See You Later! Take Care!",
    "thank you": "You're Welcome! 😊",
    "thanks": "No Problem! Happy To Help!",
    "help": "Sure! I Can Chat With You. Try Saying Hi, Hello, Or Bye.",
    "what is your name": "I'm Your Personal AI Assistant 🤖",
    "who are you": "I'm A Simple Bot Created To Chat With You!",
    "joke": "Why Did The Computer Show Up At Work Late? It Had A Hard Drive! 😂",
    "tell me a joke": "I Would Tell You A UDP Joke, But You Might Not Get It! 😄",
    "weather": "I Can't Check The Real Weather Yet, But I Hope It's Nice Outside! ☀️",
    "time": "I Can't See The Real Time, But Your Device Clock Can! ⏰",
    "date": "Check Your Device! But Remember, Every Day Is A Good Day! 📅",
    "how old are you": "I'm Timeless! 😉",
    "i love you": "I'm Flattered! But I'm Just A Bot 😅",
    "sorry": "No Worries! Everyone Makes Mistakes 😌",
    "ok": "Okay! Got It.",
    "thanks a lot": "You're Very Welcome! 😊",
    "good": "Glad To Hear That! 😄",
    "bad": "Oh No! Hope Things Get Better Soon.",
    "who created you": "I Was Created By A Human Developer Using Python And Tkinter!"
}

# === Send Message Function ===
def send_message():
    user_msg = user_entry.get().lower()  # get the user message
    chat_area.config(state="normal")
    chat_area.insert(tk.END, f"You : {user_msg}\n")  # show user message
    user_entry.delete(0, tk.END)  # clear entry box

    # check response from dictionary
    response = responses.get(user_msg, "Sorry, I didn't understand that.")
    chat_area.insert(tk.END, f"Bot : {response}\n\n")  # show bot message
    chat_area.config(state="disabled")
    chat_area.see(tk.END)  # scroll to the bottom


# === USER ENTRY BOX ===
user_entry = tk.Entry(
    input_frame,
    bg="#334155", fg="white",
    font=("Courier", 10),
    bd=0,
    insertbackground="white"
)
user_entry.grid(row=0, column=0, padx=10, pady=10, ipady=6, sticky="ew")
user_entry.bind("<Return>", lambda event: send_message())

# === SEND BUTTON ===
send_button = tk.Button(
    input_frame,
    text="➤",
    bg="#3b82f6", fg="white",
    font=("Courier", 12, "bold"),
    bd=0,
    width=4,
    activebackground="#2563eb",
)
send_button.grid(row=0, column=1, padx=10, pady=10)
send_button.config(command=send_message)

# run the window
window.mainloop()