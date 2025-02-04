from tkinter import *


class Converter():
    """
    Temperature Conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter",
                                  font="Arial 16 bold")
        self.temp_heading.grid(row=0)

        instructions = "Type in the amount of temperature you want to convert and then press one of the buttons to " \
                       "convert it to either °C or °F"
        self.temp_instructions = Label(self.temp_frame, text=instructions,
                                       wraplength=250, width=40, justify="left",
                                       font="Arial 10")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font="Arial 14")
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error, fg="red")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Button list (button text | bg colour |command | row | column)
        button_list = [
            ["To Celsius", "purple", "", 0, 0],
            ["To Fahrenheit", "green", "", 0, 1],
            ["Help / Info", "orange", "", 1, 0],
            ["History / Export", "blue", "", 1, 1]
        ]

        #  List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="white", font="Arial 12 bold",
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # Retrieve history / export button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
