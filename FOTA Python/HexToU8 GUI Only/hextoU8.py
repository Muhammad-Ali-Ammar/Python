# input_file_path = '/home/muhammad/Desktop/embedded/NTI TASK/Python WorkSpace/HexToU8/BLD_App.hex'
# output_file_path = '/home/muhammad/Desktop/embedded/NTI TASK/Python WorkSpace/HexToU8/output.txt'

# def hex_line_to_decimal_list(line):
#     # Remove the ":" at the beginning of the line
#     hex_values = line[1:].strip()
    
#     # Split the line into pairs of hexadecimal digits
#     hex_pairs = [hex_values[i:i+2] for i in range(0, len(hex_values), 2)]
    
#     # Convert each pair to decimal and join them with commas
#     decimal_list = ', '.join(str(int(pair, 16)) for pair in hex_pairs)
    
#     return decimal_list

# with open(input_file_path, 'r') as file:
#     lines = file.readlines()

# with open(output_file_path, 'w') as output_file:
#     # Start the file with an opening curly brace and newline
#     output_file.write('{\n')

#     # Process all lines
#     for i, line in enumerate(lines):
#         # Write each converted decimal value to the output file on a new line, followed by a comma
#         output_file.write('  ' + hex_line_to_decimal_list(line))
#         if i != len(lines) - 1:
#             output_file.write(',\n')

#     # End the file with a closing curly brace and newline
#     output_file.write('\n}\n')










# import tkinter as tk
# from tkinter import filedialog
# import os
# from PIL import Image, ImageTk
# import platform


# def resize_image(Copy_Img, Copy_Height, Copy_Weight):
#     Loc_Size = (Copy_Height, Copy_Weight)
#     Loc_ResizedImg = Copy_Img.resize(Loc_Size, Image.LANCZOS)
#     return ImageTk.PhotoImage(Loc_ResizedImg)


# def Convert_HexLineToDecimalList(Copy_Line):
#     # Remove the ":" at the beginning of the line
#     Loc_HexValuList = Copy_Line[1:].strip()

#     # Split the line into pairs of hexadecimal digits
#     Loc_HexPairs = [Loc_HexValuList[i:i+2] for i in range(0, len(Loc_HexValuList), 2)]

#     # Convert each pair to decimal and join them with commas
#     Loc_DecimalList = ', '.join(str(int(pair, 16)) for pair in Loc_HexPairs)

#     return Loc_DecimalList


# class ProjectWindow:
#     def __init__(self, Copy_Root):
#         self.Copy_Root = Copy_Root
#         self.Copy_Root.title("Hex to Code Generator")
#         self.text_by_Eng = tk.Label(Copy_Root, text="By Eng: Muhammad (Ali) Amamr ", fg="blue", font=("Arial", 21, "bold")).place(x=110, y=660)

#         # Image
#         Loc_ImagePath = "HexToU8/photo.png"  # Replace with the path to your image file
#         original_img = Image.open(Loc_ImagePath)
#         Loc_ResizedImage = resize_image(original_img, 500, 500)  # Set your desired height and width
#         self.img_label = tk.Label(Copy_Root, image=Loc_ResizedImage)
#         self.img_label.image = Loc_ResizedImage  # Keep a reference to prevent the image from being garbage collected
#         self.img_label.place(x=100, y=120)  # Adjust x and y as needed

#         # Input File
#         tk.Label(Copy_Root, text="Input File:").pack()
#         self.input_file_entry = tk.Entry(Copy_Root, width=50)
#         self.input_file_entry.pack()

#         # Browse Button
#         self.browse_button = tk.Button(Copy_Root, text="Browse", command=self.choose_input_file)
#         self.browse_button.pack()
#         self.browse_button.place(x=300, y=60)  # Adjust x and y as needed

#         # Generate Button
#         self.generate_button = tk.Button(Copy_Root, text="Generate Code", command=self.generate_code)
#         self.generate_button.pack()
#         self.generate_button.place(x=270, y=90)  # Adjust x and y as needed

#         # Result Label
#         self.result_label = tk.Label(Copy_Root, text="")
#         self.result_label.pack()

#     def process_file(self, input_file_path):
#         # Generate the output file name based on the input file name and directory
#         output_file_path = os.path.join(os.path.dirname(input_file_path), "output.txt")

#         with open(input_file_path, 'r') as file:
#             lines = file.readlines()

#         with open(output_file_path, 'w') as output_file:
#             # Add the prefix
#             output_file.write('unsigned char Converted_Code[]={\n')

#             # Process all lines
#             for i, line in enumerate(lines):
#                 # Write each converted decimal value to the output file on a new line, followed by a comma
#                 output_file.write('  ' + Convert_HexLineToDecimalList(line))
#                 if i != len(lines) - 1:
#                     output_file.write(',\n')

#             # Add the suffix
#             output_file.write('};\n')

#         return output_file_path

#     def choose_input_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[('Hex Files', '*.hex')])
#         self.input_file_entry.delete(0, tk.END)
#         self.input_file_entry.insert(0, file_path)

#     def generate_code(self):
#         input_file_path = self.input_file_entry.get()

#         if input_file_path:
#             output_file_path = self.process_file(input_file_path)
#             self.result_label.config(text=f'Code generated successfully. Output file: {output_file_path}')
            
#         # # Open the text file with the default text editor on Linux
#         # if platform.system() == 'Linux': 
#         #     os.system(f'gedit {output_file_path}')
#         # else:
#         #      self.result_label.config(text='Please choose an input file.')



# # Welcome Message
# print("Welcome To The Project")

# # Create the main window
# root = tk.Tk()
# root.geometry("700x700")  # Set the window size (width x height)

# # Create an instance of the ProjectWindow class
# app = ProjectWindow(root)

# # Start the GUI event loop
# root.mainloop()






###################################################################################################################### 



# import tkinter as tk
# from tkinter import filedialog
# import os
# from PIL import Image, ImageTk

# def resize_image(Copy_Img, Copy_Height, Copy_Weight):
#     Loc_Size = (Copy_Height, Copy_Weight)
#     Loc_ResizedImg = Copy_Img.resize(Loc_Size, Image.LANCZOS)
#     return ImageTk.PhotoImage(Loc_ResizedImg)

# def Convert_HexLineToDecimalList(Copy_Line):
#     Loc_HexValuList = Copy_Line[1:].strip()
#     Loc_HexPairs = [Loc_HexValuList[i:i+2] for i in range(0, len(Loc_HexValuList), 2)]
#     Loc_DecimalList = ', '.join(str(int(pair, 16)) for pair in Loc_HexPairs)
#     return Loc_DecimalList

# class ProjectWindow:
#     def __init__(self, Copy_Root):
#         self.Copy_Root = Copy_Root
#         self.Copy_Root.title("Hex to Code Generator")
#         self.text_by_Eng = tk.Label(Copy_Root, text="By Eng: Muhammad (Ali) Amamr ", fg="blue", font=("Arial", 21, "bold")).place(x=110, y=660)

#         # Image
#         Loc_ImagePath = "HexToU8/photo.png"  # Replace with the path to your image file
#         original_img = Image.open(Loc_ImagePath)
#         Loc_ResizedImage = resize_image(original_img, 500, 500)  # Set your desired height and width
#         self.img_label = tk.Label(Copy_Root, image=Loc_ResizedImage)
#         self.img_label.image = Loc_ResizedImage  # Keep a reference to prevent the image from being garbage collected
#         self.img_label.place(x=100, y=120)  # Adjust x and y as needed

#         # Input File
#         tk.Label(Copy_Root, text="Input File:").pack()
#         self.input_file_entry = tk.Entry(Copy_Root, width=50)
#         self.input_file_entry.pack()

#         # Browse Button
#         self.browse_button = tk.Button(Copy_Root, text="Browse", command=self.choose_input_file)
#         self.browse_button.pack()
#         self.browse_button.place(x=300, y=60)  # Adjust x and y as needed

#         # Generate Button
#         self.generate_button = tk.Button(Copy_Root, text="Generate Code", command=self.generate_code)
#         self.generate_button.pack()
#         self.generate_button.place(x=270, y=90)  # Adjust x and y as needed

#         # Result Label
#         self.result_label = tk.Label(Copy_Root, text="")
#         self.result_label.pack()

#         # Variables to store fifth and sixth bytes
#         self.fifth_byte = '00'
#         self.sixth_byte = '00'

#     def process_line(self, line):
#         # Check if the fourth byte is 4
#         if int(line[7:9], 16) == 4:
#             # Save fifth and sixth bytes
#             self.fifth_byte = line[9:11]
#             self.sixth_byte = line[11:13]
#             return None  # Skip this line
#         else:
#             # Process line and insert saved fifth and sixth bytes, excluding the fourth byte
#             output_line = f'{int(line[1:3], 16)}, {int(self.fifth_byte, 16)}, {int(self.sixth_byte, 16)}, '
#             output_line += ', '.join(str(int(line[i:i+2], 16)) for i in range(5, len(line)-2, 2))
#             return output_line

#     def process_file(self, input_file_path):
#         # Generate the output file name based on the input file name and directory
#         output_file_path = os.path.join(os.path.dirname(input_file_path), "output.txt")

#         with open(input_file_path, 'r') as file:
#             lines = file.readlines()

#         with open(output_file_path, 'w') as output_file:
#             # Add the prefix
#             output_file.write('unsigned char Converted_Code[]={\n')

#             # Process all lines
#             for i, line in enumerate(lines):
#                 processed_line = self.process_line(line)
#                 if processed_line is not None:
#                     output_file.write('  ' + processed_line)
#                     if i != len(lines) - 1:
#                         output_file.write(',\n')

#             # Add the suffix
#             output_file.write('};\n')

#         return output_file_path

#     def choose_input_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[('Hex Files', '*.hex')])
#         self.input_file_entry.delete(0, tk.END)
#         self.input_file_entry.insert(0, file_path)

#     def generate_code(self):
#         input_file_path = self.input_file_entry.get()

#         if input_file_path:
#             output_file_path = self.process_file(input_file_path)
#             self.result_label.config(text=f'Code generated successfully. Output file: {output_file_path}')

# # Welcome Message
# print("Welcome To The Project")

# # Create the main window
# root = tk.Tk()
# root.geometry("700x700")  # Set the window size (width x height)

# # Create an instance of the ProjectWindow class
# app = ProjectWindow(root)

# # Start the GUI event loop
# root.mainloop()





######################################################################################################################



# import tkinter as tk
# from tkinter import filedialog
# import os
# from PIL import Image, ImageTk

# def resize_image(img, height, width):
#     size = (height, width)
#     resized_img = img.resize(size, Image.LANCZOS)
#     return ImageTk.PhotoImage(resized_img)

# class ProjectWindow:
#     def __init__(self, Copy_Root):
#         self.Copy_Root = Copy_Root
#         self.Copy_Root.title("Hex to Code Generator")
#         self.Madey = tk.Label(Copy_Root, text="By: Eng/ Muhammad (Ali) Ammar ", fg="blue", font=("Arial", 21, "bold")).place(x=100, y=650)

#         # Image
#         Loc_ImagePath = "HexToU8/Escanor.png"
#         Loc_OrigrnalImage = Image.open(Loc_ImagePath)
#         resized_img = resize_image(Loc_OrigrnalImage, 450, 300)
#         self.img_label = tk.Label(Copy_Root, image=resized_img)
#         self.img_label.image = resized_img
#         self.img_label.place(x=100, y=0)


#         # Data Entry Widget BaudRate
#         self.BaudrateLabel =tk.Label(Copy_Root, text="Enter BaudRate:")
#         self.BaudrateLabel.place(x = 10, y = 320)
#         self.BaudrateDataEntry = tk.Text(Copy_Root, height=1, width=10)
#         self.BaudrateDataEntry.place(x = 120, y = 320)

#         # Input Text File
#         self.Lob_TextInputFile = tk.Label(Copy_Root, text="Input Hex File:")
#         self.Lob_TextInputFile.place(x = 10, y = 350)
        
#         self.Loc_WidgetInputFileEntry = tk.Entry(Copy_Root, width=40)
#         self.Loc_WidgetInputFileEntry.place(x = 120, y = 350)

#         # Generate Button
#         self.Loc_GenerateButton = tk.Button(Copy_Root, text="Generate Code", command=self.GenerateButton_ISR)
#         self.Loc_GenerateButton.place(x=190, y=420)

#         # Browse Button
#         self.Loc_BrowseButton = tk.Button(Copy_Root, text="Browse", command=self.BrowseButton_ISR)
#         self.Loc_BrowseButton.place(x=220, y=380)

#         # Ok Button
#         self.Loc_OkButton = tk.Button(Copy_Root, text="  Ok  ", command=self.Ok_ISR)
#         self.Loc_OkButton.place(x=220, y=500)

#         # Result Label
#         self.result_label = tk.Label(Copy_Root, text="")
#         self.result_label.place(x=220, y=450)

#         # Variables to store fifth and sixth bytes
#         self.fifth_byte = '00'
#         self.sixth_byte = '00'

#     def process_line(self, line):
#         try:
#             fourth_byte = int(line[7:9], 16)
#         except ValueError:
#             print(f"Invalid hexadecimal value in line: {line}")
#             return None

#         if fourth_byte == 4:
#             self.fifth_byte, self.sixth_byte = line[9:11], line[11:13]
#             return None
#         elif fourth_byte == 5:
#             return None
#         elif fourth_byte == 1:
#             print("End of the file")
#             return None
#         else:
#             output_line = f'{int(line[1:3], 16)}, {int(self.fifth_byte, 16)}, {int(self.sixth_byte, 16)}, '
#             output_line += ', '.join(str(int(line[i:i+2], 16)) for i in range(5, len(line)-2, 2))
#             return output_line + ', OK?'

#     def process_file(self, input_file_path):
#         output_file_path = os.path.join(os.path.dirname(input_file_path), "output.txt")

#         with open(input_file_path, 'r') as file:
#             lines = file.readlines()

#         with open(output_file_path, 'w') as output_file:
#             output_file.write('unsigned char Converted_Code[]={\n')
#             processed_lines = [self.process_line(line) for line in lines if self.process_line(line) is not None]
#             output_file.write('  ' + ',\n  '.join(processed_lines))
#             output_file.write('\n};\n')

#         return output_file_path

#     def Ok_ISR(self):
#         print("Ok Button ")

        

#     def BrowseButton_ISR(self):
#         file_path = filedialog.askopenfilename(filetypes=[('Hex Files', '*.hex')])
#         self.Loc_WidgetInputFileEntry.delete(0, tk.END)
#         self.Loc_WidgetInputFileEntry.insert(0, file_path)

#     def GenerateButton_ISR(self):
#         input_file_path = self.Loc_WidgetInputFileEntry.get()

#         if input_file_path:
#             # Get the data from the Text widget
#             entered_data = self.BaudrateDataEntry.get("1.0", tk.END)
#             print("BaudRate Is:", entered_data)

#             output_file_path = self.process_file(input_file_path)
#             self.result_label.config(text='Succeeded', fg='green')
            
            

    


# # Welcome Message
# print("Welcome To The Project")

# # Create the main window
# Loc_Root = tk.Tk()
# Loc_Root.geometry("700x700")

# # Create an instance of the ProjectWindow class
# app = ProjectWindow(Loc_Root)

# # Start the GUI event loop
# Loc_Root.mainloop()




import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

def resize_image(Copy_Image, Copy_Height, Copy_Weight):
    Loc_Size = (Copy_Height, Copy_Weight)
    Loc_ResizedImage = Copy_Image.resize(Loc_Size, Image.LANCZOS)
    return ImageTk.PhotoImage(Loc_ResizedImage)

class ProjectWindow:
    def __init__(self, Copy_Root):

############################################ Set up The root Object ############################################################
        self.Copy_Root = Copy_Root
        self.Copy_Root.title("Hex to Code Generator")

############################################ Text ###########################################################################

        self.MadeBy = tk.Label(Copy_Root, text="By: Eng/ Muhammad (Ali) Ammar ", fg="blue", font=("Arial", 21, "bold")).place(x=100, y=650)
        self.SecondScreenWindow = tk.Label(Copy_Root, text="Screen Window ", fg="black", font=("Arial", 21, "bold")).place(x=900, y=20)

        # Image
        Loc_ImagePath = "HexToU8/Escanor.png"
        Loc_OrigrnalImage = Image.open(Loc_ImagePath)
        Loc_ResizedImage = resize_image(Loc_OrigrnalImage, 450, 300)
        self.Loc_ImageLabel = tk.Label(Copy_Root, image=Loc_ResizedImage)
        self.Loc_ImageLabel.image = Loc_ResizedImage
        self.Loc_ImageLabel.place(x=100, y=0)

        # BaudRate Entry
        self.BaudrateLabel = tk.Label(Copy_Root, text="Enter BaudRate:")
        self.BaudrateLabel.place(x=10, y=320)
        self.BaudrateDataEntry = tk.Text(Copy_Root, height=1, width=10)
        self.BaudrateDataEntry.place(x=120, y=320)

        # Input Hex File Entry
        self.Lob_TextInputFile = tk.Label(Copy_Root, text="Input Hex File:")
        self.Lob_TextInputFile.place(x=10, y=350)
        self.Loc_WidgetInputFileEntry = tk.Entry(Copy_Root, width=40)
        self.Loc_WidgetInputFileEntry.place(x=120, y=350)

        # Generate Button
        self.Loc_GenerateButton = tk.Button(Copy_Root, text="Generate Code", command=self.GenerateButton_ISR)
        self.Loc_GenerateButton.place(x=190, y=420)

        # Browse Button
        self.Loc_BrowseButton = tk.Button(Copy_Root, text="Browse", command=self.BrowseButton_ISR)
        self.Loc_BrowseButton.place(x=220, y=380)

        # Ok Button
        self.Loc_OkButton = tk.Button(Copy_Root, text="  Ok  ", command=self.Ok_ISR)
        self.Loc_OkButton.place(x=220, y=500)

        # Result Label
        self.Loc_ResultLabel = tk.Label(Copy_Root, text="")
        self.Loc_ResultLabel.place(x=220, y=450)

        # Second Window
        self.SecondScreen = tk.Text(Copy_Root, height=37, width=95)
        self.SecondScreen.place(x=620, y=60)

        # Variables to store fifth and sixth bytes
        self.fifth_byte = '00'


############################################ Static Method ############################################################

    def voidParseLine(self, line):
        try:
            fourth_byte = int(line[7:9], 16)
        except ValueError:
            print(f"Invalid hexadecimal value in line: {line}")
            return None, None

        if fourth_byte == 4:
            self.fifth_byte = line[9:13]
            return None, None
        elif fourth_byte == 5:
            return None, None
        elif fourth_byte == 1:
            print("End of the file")
            return None, None
        else:
            SecondPartOfAddress = line[3:7]
            first_part = self.fifth_byte[0:2]
            second_part = self.fifth_byte[2:4]
            first_part1, first_part2, first_part3, first_part4 = first_part[0], first_part[1], second_part[0], second_part[1]
            ThirdPart = SecondPartOfAddress[0:2]
            ForthPart = SecondPartOfAddress[2:4]
            first_part5, first_part6, first_part7, first_part8 = ThirdPart[0], ThirdPart[1], ForthPart[0], ForthPart[1]

            Loc_DataBytesNumber = int(line[1:3], 16)
            Loc_DataBytesValues = ', '.join(str(int(line[i:i+2], 16)) for i in range(9, len(line)-3, 2))
            Loc_CheckSum = int(line[-3:], 16)

            Loc_ScreenOuputData = f'Record {self.Loc_RecondNumberCounter}:\n'
            Loc_ScreenOuputData += f'Number of Data Bytes: {Loc_DataBytesNumber}\n'
            Loc_ScreenOuputData += f'Address: 0x{first_part1}{first_part2}{first_part3}{first_part4}{first_part5}{first_part6}{first_part7}{first_part8}\n'
            Loc_ScreenOuputData += f'Data Bytes: {Loc_DataBytesValues}\n'
            Loc_ScreenOuputData += f'Check Sum: {Loc_CheckSum}\n\n'

            Loc_OutputDataForFile = f'{Loc_DataBytesNumber}, {first_part1},{first_part2},{first_part3},{first_part4},{first_part5},{first_part6},{first_part7},{first_part8}, {Loc_DataBytesValues}, {Loc_CheckSum},OK?\n'

            return Loc_ScreenOuputData, Loc_OutputDataForFile

    def voidWriting(self, input_file_path):
        Loc_OutputFilePath = os.path.join(os.path.dirname(input_file_path), "output.txt")

        with open(input_file_path, 'r') as file:
            Loc_AllRecordLines = file.readlines()

        self.SecondScreen.delete(1.0, tk.END) # remove the window on each generated code 

        with open(Loc_OutputFilePath, 'w') as Loc_OutputFile:
            Loc_OutputFile.write('unsigned char Converted_Code[]={\n')
            self.Loc_RecondNumberCounter = 1
            for Loc_Index, Loc_LineCounter in enumerate(Loc_AllRecordLines):
                processed_screen_line, processed_file_line = self.voidParseLine(Loc_LineCounter)
                if processed_screen_line is not None:
                    self.SecondScreen.insert(tk.END, processed_screen_line)
                    Loc_OutputFile.write(f'  {processed_file_line}')
                    self.Loc_RecondNumberCounter += 1

            if Loc_Index == len(Loc_AllRecordLines) - 1:
                Loc_OutputFile.seek(Loc_OutputFile.tell() - 2)
                Loc_OutputFile.truncate()

            Loc_OutputFile.write('?\n};\n')

        return Loc_OutputFilePath

    def Ok_ISR(self):
        print("Ok Button ")

    def BrowseButton_ISR(self):
        file_path = filedialog.askopenfilename(filetypes=[('Hex Files', '*.hex')])
        self.Loc_WidgetInputFileEntry.delete(0, tk.END)
        self.Loc_WidgetInputFileEntry.insert(0, file_path)

    def GenerateButton_ISR(self):
        Loc_InputFilePath = self.Loc_WidgetInputFileEntry.get()

        if Loc_InputFilePath:
            entered_data = self.BaudrateDataEntry.get("1.0", tk.END)
            print("BaudRate Is:", entered_data)

            output_file_path = self.voidWriting(Loc_InputFilePath)
            self.Loc_ResultLabel.config(text='Succeeded', fg='green')

# Welcome Message
print("Welcome To The Project")

# Create the main window
Loc_Root = tk.Tk()
Loc_Root.geometry("1400x700")

# Create an instance of the ProjectWindow class
app = ProjectWindow(Loc_Root)

# Start the GUI event loop
Loc_Root.mainloop()
