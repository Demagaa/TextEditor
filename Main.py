import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openFile():
    """Open a file for editing."""
    filePath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filePath:
        return
    txtEdit.delete(1.0, tk.END)
    with open(filePath, "r") as inputFile:
        text = inputFile.read()
        txtEdit.insert(tk.END, text)
    window.title(f"Thecleverprogrammer - {filePath}")

def saveFile():
    """Save the current file as a new file."""
    filePath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filePath:
        return
    with open(filePath, "w") as outputFile:
        text = txtEdit.get(1.0, tk.END)
        outputFile.write(text)
    window.title(f"Thecleverprogrammer - {filePath}")

window = tk.Tk()
window.title("Thecleverprogrammer")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txtEdit = tk.Text(window)
frButtons = tk.Frame(window, relief=tk.RAISED, bd=2)
btnOpen = tk.Button(frButtons, text="Open", command=openFile)
btnSave = tk.Button(frButtons, text="Save As...", command=saveFile)

btnOpen.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btnSave.grid(row=1, column=0, sticky="ew", padx=5)

frButtons.grid(row=0, column=0, sticky="ns")
txtEdit.grid(row=0, column=1, sticky="nsew")

window.mainloop()