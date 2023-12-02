from tkinter import *
import time

def display_time():
    hour = str(time.strftime("%H"))
    minute = str(time.strftime("%M"))
    second = str(time.strftime("%S"))

    if int(hour) >= 12 and int(hour) < 24 and int(minute) >= 0:
        meridiem_label.config(text="PM", fg="#ff5757")
    else:
        meridiem_label.config(text="AM", fg="#65a5ff") 

    if int(hour) > 12:
        hour = str((int(hour) - 12))
    elif int(hour) == 0:
        hour = str(12)

    hour_label.config(text=hour, fg="#333333")
    minute_label.config(text=minute, fg="#333333") 
    second_label.config(text=second, fg="#333333") 

    hour_label.after(200, display_time)

if __name__ == "__main__":
    gui_root = Tk()
    gui_root.title("Zegar Cyfrowy")
    gui_root.geometry("650x250+650+250")
    gui_root.resizable(0, 0)
    gui_root.config(bg="#f0f0f0")

    header_frame = Frame(gui_root, bg="#f0f0f0")
    body_frame = Frame(gui_root, bg="#f0f0f0")
    header_frame.pack(pady=15)
    body_frame.pack()

    header_label = Label(
        header_frame,
        text="Zegar Cyfrowy",
        font=("Helvetica", "14", "bold"),
        bg="#f0f0f0",
        fg="#333333"
    )
    header_label.pack()

    hour_label = Label(
        body_frame,
        text="00",
        font=("Helvetica", "48"),
        bg="#f0f0f0",
        fg="#333333"  # Kolor tekstu godzin
    )
    colon_label_one = Label(
        body_frame,
        text=":",
        font=("Helvetica", "48"),
        bg="#f0f0f0",
        fg="#333333"
    )
    minute_label = Label(
        body_frame,
        text="00",
        font=("Helvetica", "48"),
        bg="#f0f0f0",
        fg="#333333" 
    )
    colon_label_two = Label(
        body_frame,
        text=":",
        font=("Helvetica", "48"),
        bg="#f0f0f0",
        fg="#333333"
    )
    second_label = Label(
        body_frame,
        text="00",
        font=("Helvetica", "48"),
        bg="#f0f0f0",
        fg="#333333"
    )
    meridiem_label = Label(
        body_frame,
        text="AM",
        font=("Helvetica", "48"),
        bg="#f0f0f0",
        fg="#65a5ff"
    )

    hour_label.grid(row=0, column=0, padx=5, pady=5)
    colon_label_one.grid(row=0, column=1, padx=5, pady=5)
    minute_label.grid(row=0, column=2, padx=5, pady=5)
    colon_label_two.grid(row=0, column=3, padx=5, pady=5)
    second_label.grid(row=0, column=4, padx=5, pady=5)
    meridiem_label.grid(row=0, column=5, padx=5, pady=5)

    display_time()

    gui_root.mainloop()
