from tkinter import *
import all_constants as c
import conversion_rounding as cr
from functools import partial  # To prevent unwanted windows


class Converter:
    """
    Temperature Conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):

        """
        Temperature converter GUI
        """

        # Store the calculated answers
        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        # self.to_help_button = Button(self.temp_frame,
        #                              text="Help / Info",
        #                              bg="#CC6600",
        #                              fg="#FFFFFF",
        #                              font="Arial 14 bold",
        #                              width=12,
        #                              command=self.to_help)
        # self.to_help_button.grid(row=1, padx=5, pady=5)

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", 
                                  font="Arial 16 bold")
        self.temp_heading.grid(row=0)

        instructions = "Type in the amount of temperature you want to convert and " \
                       "then press one of the buttons to convert it to either °C or °F"
        self.temp_instructions = Label(self.temp_frame, text=instructions, wraplength=250, width=40,
                                       justify="left", font="Arial 10")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font="Arial 14")
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error, fg="blue")
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
 
        # Button list (button text | bg colour |command | row | column)
        button_list = [
            ["To Celsius", "purple", lambda:self.check_temp(c.ABS_ZERO_F), 0, 0],
            ["To Fahrenheit", "green", lambda:self.check_temp(c.ABS_ZERO_C), 0, 1],
            ["Help / Info", "orange", self.to_help, 1, 0],
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

        # Retrieve to_help button
        self.to_help_button = self.button_ref_list[2]

        # Retrieve history / export button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)



    def check_temp(self, min_temp):
        """
        Checks temperature is valid and either 
        invokes calculation function or shows error message
        """

        # Retrieve the temperature to be converted
        temp_to_convert = self.temp_entry.get()
        print("To convert: ", temp_to_convert)

        # Reset label and entry box
        self.answer_error.config(fg="blue", font="Arial 13 bold")
        self.temp_entry.config(bg="white")

        # Check if the temperature is a number and above absolute zero
        try:
            temp_to_convert = float(temp_to_convert)
            if temp_to_convert >= min_temp:
                error = ""
                self.convert(min_temp, temp_to_convert)
            else:
                error = "Too Cold"

        except ValueError:
            error = f"Please enter a number more than / equal to {min_temp}"

        # Display error message if necessary
        if error != "":
            self.answer_error.config(text=error, fg="red")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

    def convert(self, min_temp, temp_to_convert):
        """
        Converts the temperature to the desired unit
        """

        if min_temp == c.ABS_ZERO_C:
            ans = cr.to_fahrenheit(temp_to_convert)
            ans_statement = f"{temp_to_convert}°C is {ans}°F"
        else:
            ans = cr.to_celsius(temp_to_convert)
            ans_statement = f"{temp_to_convert}°F is {ans}°C"

        # Enable history button after a valid conversion
        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=ans_statement)
        self.all_calculations_list.append(ans_statement)
        print(self.all_calculations_list)

    def to_help(self):
        """
        Opens help dialogue box and disables help button
        (so that users can't create multiple help windows).

        """

        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and background color
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # Disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help
        # and enables help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        # Set up the frame
        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        # Set up heading
        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font="Arial 14 bold")
        self.help_heading_label.grid(row=0)

        help_text = ("To use the program, simply enter the temperature "
                     "you wish to convert and then choose to convert "
                     "to either degrees Celsius or Fahrenheit.. \n\n "
                     "Note that -273 degrees C (-459 F) is absolute "
                     "zero (the coldest possible temperature). If "
                     "you try to convert a temperature that is less "
                     "than -273 degrees C, you will get an error "
                     "message. \n\n To see your calculation history "
                     "and export it to a text file, please click "
                     "the 'History / Export' button.")

        # Set up text
        self.help_text_label = Label(self.help_frame,
                                     text=help_text,
                                     wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        # Set up dismiss button
        self.dismiss_button = Button(self.help_frame,
                                     font="Arial 12 bold",
                                     text="Dismiss",
                                     bg="#cc6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background color on
        # everything except the buttons
        recolor_list = [self.help_frame, self.help_heading_label,
                        self.help_text_label]

        for item in recolor_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
       Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
