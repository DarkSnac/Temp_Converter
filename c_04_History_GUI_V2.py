from tkinter import *
from functools import partial  # To prevent unwanted windows
import all_constants as c


class Converter:
    """
    Temperature Conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        # Store the calculated answers
        self.all_calculations_list = ['10.0°F is -12°C', '20.0°F is -7°C', '30.0°F is -1°C',
                                      '40.0°F is 4°C', '50.0°F is 10°C', '60.0°F is 16°C']

        # self.all_calculations_list = ['10.0°F is -12°C', '20.0°F is -7°C', '30.0°F is -1°C',
        #                               '40.0°F is 4°C', '50.0°F is 10°C']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font="Arial 14 bold",
                                        width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens help dialogue box and disables help button
        (so that users can't create multiple help windows).
        """

        HistoryExport(self, self.all_calculations_list)


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
            ["Export", "#004C99", '', 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1]
        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font='Arial 12 bold',
                                      text=btn[0], bg=btn[1],
                                      fg='#FFFFFF', width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

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
