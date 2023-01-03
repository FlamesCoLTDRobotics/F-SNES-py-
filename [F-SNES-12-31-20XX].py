import tkinter as tk
import tkinter.ttk as ttk

# Create a Tkinter window
window = tk.Tk()
window.geometry("800x800")

# Set the "Aqua" theme for the widgets
ttk.Style().theme_use("aqua")

# Add a label for displaying game titles
title_label = ttk.Label(text="SNES Emulator", font=('Helvetica', 18))
title_label.pack()

# Add a frame for displaying the emulator screen
screen_frame = ttk.Frame(width=600, height=450)
screen_frame.pack()

# Add a label for displaying debug information
debug_label = ttk.Label(text="Debug information will go here", font=('Helvetica', 12))
debug_label.pack()

# Add a button for starting the emulator
def start_emulator():
  # Call the C script to start the emulator
  import subprocess
  subprocess.run(["sneshle"])

start_button = ttk.Button(text="Start Emulator", command=start_emulator)
start_button.pack()

# Start the event loop
window.mainloop()
