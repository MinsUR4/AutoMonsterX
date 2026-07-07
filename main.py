import os
import sys
import subprocess
from tkinter import messagebox

def run_setup_if_needed():
    # 1. Find the hidden folder where PyInstaller put the .bat file
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    bat_file_path = os.path.join(base_path, "install_dependencies.bat")

    # 2. Run the bat file if it exists
    if os.path.exists(bat_file_path):
        try:
            # Open a temporary console ONLY for the installation process 
            # so the user can see the download progress.
            if os.name == 'nt':  # If running on Windows
                subprocess.run(
                    [bat_file_path], 
                    creationflags=subprocess.CREATE_NEW_CONSOLE, 
                    check=True
                )
            else:
                subprocess.run([bat_file_path], shell=True, check=True)
                
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Setup Error", f"Installation failed or was cancelled.\nError: {e}")
            sys.exit(1)

run_setup_if_needed()

try:
    from controller_gui import ControllerGUI
    from wakepy import keep
except ImportError as e:
    messagebox.showerror("Import Error", f"A dependency is still missing. Setup may have failed.\n\n{e}")
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