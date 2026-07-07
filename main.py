import os
import sys
from tkinter import messagebox

# No more setup checks! The .exe will already have these inside it.
try:
    from controller_gui import ControllerGUI
    from wakepy import keep
except ImportError as e:
    messagebox.showerror("Import Error", f"A dependency failed to bundle during compilation.\n\n{e}")
    sys.exit(1)


def main():
    try:
        # Check if app was launched after update
        updated = len(sys.argv) > 1 and sys.argv[1] == "updated"

        with keep.presenting():
            app = ControllerGUI()
            app.mainloop()

    except KeyboardInterrupt:
        return

    except Exception as e:
        if os.path.exists("debug.ban"):
            raise e

        messagebox.showerror(
            "Error",
            str(e)
        )


if __name__ == '__main__':
    main()