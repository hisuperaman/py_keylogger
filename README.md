# py_keylogger
Simple keylogger in Python

<h2>To make the script active as the Windows boots</h3>
<p>1. Create executable of this script using -</p>
<p>    pyinstaller --name anyname main.py</p>
<p>2. Add the executable to startup of Windows -</p>
<p>    Copy the executable from /dist/anyname/anyname.exe</p>
<p>    Press, Ctrl + R</p>
<p>    Type, shell:startup</p>
<p>    Paste shortcut in the Startup folder</p>
<p>3. Restart your computer</p>
<br>
<p>The log file will be saved in the same directory as the actual script/executable</p>