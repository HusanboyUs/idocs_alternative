# Open-source time tracking app (Timlog)

Please be aware that application building process has not finished yet

## How to install?

1.Download the branch files
```
git clone <url-of-main-branch>
```
2. Create and activate venv on ur local dir

```
python3 -m venv venv

```
activate on Windows powershell

```
venv/Scripts/activate

```
or cmd 
```
venv/Scripts/activate.bat
```
activate on Mac terminal

```
venv/bin/activate

```
4. IMPORTANT: create modal database:
on the same branch with modal.py open terminal and
```
python3
```
and

```
from modal import Modal
a= Modal()
a.create_table()
```



