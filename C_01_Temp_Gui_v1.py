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

        instructions = "Type in the amount of temperature you want to convert and then press one of the buttons to convert it to either °C or °F"
        self.temp_instructions = Label(self.temp_frame, text=instructions, 
                                        wrap=250, width=40, justify="left", 
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

        self.to_c_button = Button(self.button_frame, text="To Celsius", 
                                  bg="purple", fg="white",
                                  font="Arial 12 bold", width=15)
        self.to_c_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_f_button = Button(self.button_frame, text="To Fahrenheit", 
                                  bg="green", fg="white",
                                  font="Arial 12 bold", width=15)
        self.to_f_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_frame, text="Help / Info", 
                                  bg="orange", fg="white",
                                  font="Arial 12 bold", width=15)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_export_button = Button(self.button_frame, text="History / Export",
                                            bg="blue", fg="white",
                                            font="Arial 12 bold", width=15)
        self.history_export_button.grid(row=1, column=1, padx=5, pady=5)





# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
