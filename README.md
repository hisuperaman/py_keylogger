# py_keylogger
Simple keylogger in Python

<h4>To make the script active as the Windows boots</h4>
1. Create executable of this script using -
    pyinstaller --name anyname main.py
2. Add the executable to startup of Windows -
    Copy the executable from /dist/anyname/anyname.exe
    Press, Ctrl + R
    Type, shell:startup
    Paste shortcut in the Startup folder
3. Restart your computer

The log file will be saved in the same directory as the actual script/executable