import speech_recognition as sr
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog


class GUI:
    def __init__(self):
        # Create the GUI
        self.file = None

        self.mainW = tk.Tk()
        self.mainW.title("Audio to Text Converter")
        self.mainW.geometry("500x200")
        self.mainW.eval('tk::PlaceWindow %s center' % self.mainW.winfo_pathname(self.mainW.winfo_id()))
        self.mainW.protocol("WM_DELETE_WINDOW", self.mainW.destroy)

        self.topF = tk.Frame(self.mainW)
        self.mainF = tk.Frame(self.mainW)
        self.bottomF = tk.Frame(self.mainW)
        self.label = tk.Label(self.topF, text="Wav to txt converter")

        self.instructions = tk.Label(self.mainF, text="Select a .wav file to transcribe")
        self.browseB = tk.Button(self.mainF, text="Browse", command=self.getFile)

        self.filePath = tk.Label(self.bottomF, text="")
        self.my_button = tk.Button(self.bottomF, text="Convert", command=self.convertToTxt)

        self.label.pack()
        self.instructions.pack()
        self.browseB.pack()
        self.filePath.pack()
        self.my_button.pack()
        self.topF.pack()
        self.mainF.pack()
        self.bottomF.pack()
        tk.mainloop()

    def convertToTxt(self):
        # Initialize recognizer class (for recognizing the speech)
        if self.file is None:
            tkinter.messagebox.showinfo("Error", "No file selected")
            return
        r = sr.Recognizer()
        newFile = open(self.filePath.cget("text")[:-3] + 'txt', 'w')
        with sr.AudioFile(self.filePath.cget("text")) as source:
            audio_text = r.listen(source)
            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                text = r.recognize_google(audio_text)
                tk.messagebox.showinfo('Response', 'File successfully transcribed!')
                newFile.write(text)
            except:
                tk.messagebox.showinfo('Response', 'Sorry, could not recognize the audio, try again later.')
        newFile.close()

    def getFile(self):
        # Open file dialog
        self.file = tkinter.filedialog.askopenfilename(initialdir='/', title='Select file',
                                                       filetypes=(('wav files', '*.wav'), ('all files', '*.*')))
        # Write the file path to the text box
        self.filePath.config(text=self.file)


if __name__ == "__main__":
    gui = GUI()
