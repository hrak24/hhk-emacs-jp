import sys
import os
import datetime

import pyauto
from keyhac import *

HENKAN_CODE = "(28)"
MUHENKAN_CODE = "(29)"

not_emacs_target = ["bash.exe",               # WSL
                    "ubuntu.exe",             # WSL
                    "ubuntu1604.exe",         # WSL
                    "ubuntu1804.exe",         # WSL
                    "ubuntu2004.exe",         # WSL
                    "debian.exe",             # WSL
                    "kali.exe",               # WSL
                    "SLES-12.exe",            # WSL
                    "openSUSE-42.exe",        # WSL
                    "openSUSE-Leap-15-1.exe",  # WSL
                    "mstsc.exe",              # Remote Desktop
                    "WindowsTerminal.exe",    # Windows Terminal
                    "mintty.exe",             # mintty
                    "Cmder.exe",              # Cmder
                    "ConEmu.exe",             # ConEmu
                    "ConEmu64.exe",           # ConEmu
                    "emacs.exe",              # Emacs
                    "emacs-X11.exe",          # Emacs
                    "emacs-w32.exe",          # Emacs
                    "gvim.exe",               # GVim
                    "Code.exe",               # VSCode
                    "xyzzy.exe",              # xyzzy
                    "VirtualBox.exe",         # VirtualBox
                    "XWin.exe",               # Cygwin/X
                    "XWin_MobaX.exe",         # MobaXterm/X
                    "Xming.exe",              # Xming
                    "vcxsrv.exe",             # VcXsrv
                    "X410.exe",               # X410
                    "putty.exe",              # PuTTY
                    "ttermpro.exe",           # TeraTerm
                    "MobaXterm.exe",          # MobaXterm
                    "TurboVNC.exe",           # TurboVNC
                    "vncviewer.exe",          # UltraVNC
                    "vncviewer64.exe",        # UltraVNC
                    ]


def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "C:\\Users\\5031842\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            shellExecute( None, "notepad.exe", '"%s"'% path, "" )
        keymap.editor = editor

    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "MS Gothic", 12 )

    # Theme
    keymap.setTheme("black")

    # --------------------------------------------------------------------

    # Simple key replacement
    keymap.replaceKey( "LWin", 235 )
    keymap.replaceKey( "RWin", 255 )
    keymap.replaceKey( MUHENKAN_CODE, 235 )
    keymap.replaceKey( HENKAN_CODE, 255 )

    # User modifier key definition
    keymap.defineModifier( 235, "User0" )
    keymap.defineModifier( 255, "User1" )

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # IME mode switch
        keymap_global[ "O-235" ] = MUHENKAN_CODE           # Muhenkan
        keymap_global[ "O-255" ] = HENKAN_CODE             # Henkan

        # Windows key combination
        keymap_global[ "U1-E" ] = "W-E"                   # Explorer
        keymap_global[ "U1-A" ] = "W-A"                   # Action center
        keymap_global[ "U1-D" ] = "W-D"                   # Desktop
        keymap_global[ "U1-M" ] = "W-M"                   # Minimize
        keymap_global[ "U0-0" ] = "W-0"                   # Launcher
        keymap_global[ "U0-1" ] = "W-1"                   # Launcher
        keymap_global[ "U0-2" ] = "W-2"                   # Launcher
        keymap_global[ "U0-3" ] = "W-3"                   # Launcher
        keymap_global[ "U0-4" ] = "W-4"                   # Launcher
        keymap_global[ "U0-5" ] = "W-5"                   # Launcher
        keymap_global[ "U0-6" ] = "W-6"                   # Launcher
        keymap_global[ "U0-7" ] = "W-7"                   # Launcher
        keymap_global[ "U0-8" ] = "W-8"                   # Launcher
        keymap_global[ "U0-9" ] = "W-9"                   # Launcher
        keymap_global[ "U1-0" ] = "W-0"                   # Launcher
        keymap_global[ "U1-1" ] = "W-1"                   # Launcher
        keymap_global[ "U1-2" ] = "W-2"                   # Launcher
        keymap_global[ "U1-3" ] = "W-3"                   # Launcher
        keymap_global[ "U1-4" ] = "W-4"                   # Launcher
        keymap_global[ "U1-5" ] = "W-5"                   # Launcher
        keymap_global[ "U1-6" ] = "W-6"                   # Launcher
        keymap_global[ "U1-7" ] = "W-7"                   # Launcher
        keymap_global[ "U1-8" ] = "W-8"                   # Launcher
        keymap_global[ "U1-9" ] = "W-9"                   # Launcher

        # Cursor move
        keymap_global[ "U0-OpenBracket" ] = "Up"                   # Windows snap
        keymap_global[ "U0-Slash" ] = "Down"                   # Windows snap
        keymap_global[ "U0-Semicolon" ] = "Left"                   # Windows snap
        keymap_global[ "U0-Quote" ] = "Right"                   # Windows snap

        # Window snap
        keymap_global[ "U0-S-OpenBracket" ] = "W-Up"                   # Windows snap
        keymap_global[ "U0-S-Slash" ] = "W-Down"                   # Windows snap
        keymap_global[ "U0-S-Semicolon" ] = "W-Left"                   # Windows snap
        keymap_global[ "U0-S-Quote" ] = "W-Right"                   # Windows snap

        # Etc
        keymap_global[ "C-OpenBracket" ] = "Esc", MUHENKAN_CODE            # Vim escape


    # USER0-E : Activate specific window or launch application if the window doesn't exist
    if 1:
        def command_ActivateOrExecuteNotepad():
            wnd = Window.find( "Notepad", None )
            if wnd:
                if wnd.isMinimized():
                    wnd.restore()
                wnd = wnd.getLastActivePopup()
                wnd.setForeground()
            else:
                executeFunc = keymap.ShellExecuteCommand( None, "notepad.exe", "", "" )
                executeFunc()

        # keymap_global[ "U0-E" ] = command_ActivateOrExecuteNotepad


    # Ctrl-Tab : Switching between console related windows
    if 1:

        def isConsoleWindow(wnd):
            if wnd.getClassName() in ("PuTTY","MinTTY","CkwWindowClass"):
                return True
            return False

        keymap_console = keymap.defineWindowKeymap( check_func=isConsoleWindow )

        def command_SwitchConsole():

            root = pyauto.Window.getDesktop()
            last_console = None

            wnd = root.getFirstChild()
            while wnd:
                if isConsoleWindow(wnd):
                    last_console = wnd
                wnd = wnd.getNext()

            if last_console:
                last_console.setForeground()

        keymap_console[ "C-TAB" ] = command_SwitchConsole


    # USER0-Space : Application launcher using custom list window
    if 1:
        def command_PopApplicationList():

            # If the list window is already opened, just close it
            if keymap.isListWindowOpened():
                keymap.cancelListWindow()
                return

            def popApplicationList():

                applications = [
                    ( "Notepad", keymap.ShellExecuteCommand( None, "notepad.exe", "", "" ) ),
                    ( "Paint", keymap.ShellExecuteCommand( None, "mspaint.exe", "", "" ) ),
                ]

                websites = [
                    ( "Google", keymap.ShellExecuteCommand( None, "https://www.google.co.jp/", "", "" ) ),
                    ( "Facebook", keymap.ShellExecuteCommand( None, "https://www.facebook.com/", "", "" ) ),
                    ( "Twitter", keymap.ShellExecuteCommand( None, "https://twitter.com/", "", "" ) ),
                ]

                listers = [
                    ( "App",     cblister_FixedPhrase(applications) ),
                    ( "WebSite", cblister_FixedPhrase(websites) ),
                ]

                item, mod = keymap.popListWindow(listers)

                if item:
                    item[1]()

            # Because the blocking procedure cannot be executed in the key-hook,
            # delayed-execute the procedure by delayedCall().
            keymap.delayedCall( popApplicationList, 0 )

        keymap_global[ "U0-Space" ] = command_PopApplicationList


    # Execute the System commands by sendMessage
    if 1:
        def close():
            wnd = keymap.getTopLevelWindow()
            wnd.sendMessage( WM_SYSCOMMAND, SC_CLOSE )

        def screenSaver():
            wnd = keymap.getTopLevelWindow()
            wnd.sendMessage( WM_SYSCOMMAND, SC_SCREENSAVE )

        keymap_global[ "U0-C" ] = close              # Close the window
        keymap_global[ "U0-S" ] = screenSaver        # Start the screen-saver


    # For Edit box, assigning Delete to C-D, etc
    if 1:
        def isEmacsTarget(wnd):
            if wnd.getProcessName() not in not_emacs_target:
                return True
            return False
        keymap_edit = keymap.defineWindowKeymap( check_func=isEmacsTarget)

        keymap_edit[ "U0-D" ] = "Delete"              # Delete
        keymap_edit[ "U0-H" ] = "Back"                # Backspace
        keymap_edit[ "U0-K" ] = "S-End","C-X"         # Removing following text
        keymap_edit[ "U0-U" ] = "Home","S-End","C-X"  # Removing line
        keymap_edit[ "U0-P" ] = "Up"                  # Move cursor up
        keymap_edit[ "U0-N" ] = "Down"                # Move cursor down
        keymap_edit[ "U0-F" ] = "Right"               # Move cursor right
        keymap_edit[ "U0-B" ] = "Left"                # Move cursor left
        keymap_edit[ "U0-A" ] = "Home"                # Move to beginning of line
        keymap_edit[ "U0-E" ] = "End"                 # Move to end of line

        keymap_edit[ "U0-S-P" ] = "S-Up"              # Move cursor up
        keymap_edit[ "U0-S-N" ] = "S-Down"            # Move cursor down
        keymap_edit[ "U0-S-F" ] = "S-Right"           # Move cursor right
        keymap_edit[ "U0-S-B" ] = "S-Left"            # Move cursor left
        keymap_edit[ "U0-S-A" ] = "S-Home"            # Move to beginning of line
        keymap_edit[ "U0-S-E" ] = "S-End"             # Move to end of line

        keymap_edit[ "U0-C" ] = "C-c"                 # Copy
        keymap_edit[ "U0-V" ] = "C-v"                 # Paste

    # VScode org-mode
    if 1:
        def isVSC(wnd):
            if wnd.getProcessName() == "Code.exe":
                return True
            return False
        keymap_vsc = keymap.defineWindowKeymap( check_func=isVSC)
        keymap_vsc[ "C-A-O" ] = "C-A-O", MUHENKAN_CODE              # Disable IME to input org-mode command
