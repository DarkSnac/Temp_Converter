from tkinter import *
import all_constants as c
import conversion_rounding as cr
from functools import partial  # To prevent unwanted windows
from datetime import date


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
            ["History / Export", "blue", self.to_history, 1, 1]
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

    def to_history(self):
        """
        Opens help dialogue box and disables help button
        (so that users can't create multiple help windows).
        """

        HistoryExport(self, self.all_calculations_list)


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


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner, calculations):
        # setup dialogue box
        self.history_box = Toplevel()

        # Disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history
        # and enables history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        # Set up the frame
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Background colour and text for calculation area
        if len(calculations) <= c.MAX_CALCS:
            calc_back = '#D5E8D4'
            calc_amount = 'all your'
        else:
            calc_back = '#ffe6cc'
            calc_amount = f'your recent calculations - ' \
                          f'showing {c.MAX_CALCS} / {len(calculations)}'

        # Strings for long labels
        history_text = f"Below are {calc_amount} calculations " \
                       f"(to the nearest degree). "

        # Create string from calculations list (newest calculations first)
        newest_first_string = ''

        newest_first_list = list(reversed(calculations))

        # Last item added in outside the for loop is so that the spacing is correct
        if len(newest_first_list) <= c.MAX_CALCS:
            for item in newest_first_list[: - 1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[- 1]

        # IF we have more than five items...
        else:
            for item in newest_first_list[:c.MAX_CALCS - 1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.MAX_CALCS - 1]

        export_instruction = "Please push <Export> to save your calculations in a text file" \
                             "If the filename already exists, it will be overwritten!"

        # label list (label text | forman | bg)
        history_label_list = [
            ["History / Export", "Arial 16 bold", None],
            [history_text, "Arial 11", None],
            [newest_first_string, "Arial 14", calc_back],
            [export_instruction, "Arial 11", None],
        ]

        history_label_ref = []
        for count, item in enumerate(history_label_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300,
                               justify='left',
                               pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # Make frame to hold buttons (two columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        # Button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1]
        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font='Arial 12 bold',
                                      text=btn[0], bg=btn[1],
                                      fg='#FFFFFF', width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def export_data(self, calculations):
        # **** Get current date for heading and filename ****
        today = date.today()

        # Get day month and year as individual strings
        day = today.strftime('%d')
        month = today.strftime('%m')
        year = today.strftime('%y')

        file_name = f"Temperatures_{year}_{month}_{day}"

        # Edit label so users know that their export has been done
        success_string = f"Export Successful! The file is called " \
                         f"{file_name}.txt"
        self.export_filename_label.config(fg="#009900", text=success_string,
                                          font="Arial 12 bold")

        write_to = f"{file_name}.txt"

        with open(write_to, 'w') as text_file:
            text_file.write("***** Temperature Calculations *****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculations history (oldest to newest)...\n")

            # Write the item to file
            for item in calculations:
                text_file.write(item)
                text_file.write('\n')

    def close_history(self, partner):
        """
       Closes history dialogue box (and enables history button)
        """
        # Put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
