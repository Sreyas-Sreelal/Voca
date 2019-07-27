# Voca
Voca is a voice assistant written in Python.I just made this project for fun and to automate some tasks in my machine.
It uses trained aiml files of ALICE bot as the basis for simple intelligence.I'm hoping to improve this as i get some time and yes,any kind of contribution to this project is welcome.

## Running
To run Voca just run the main.py file
```bash
python main.py
```
and speak

You can also import the project as a package and use the run method to initialize Voca.
## Adding commands
You can easily add custom command.Just add a new file
For example

**cmd_ping.py**
```Python
def execute(voca_say,listen_and_understand,heard=""):
    voca_say("pong")
```
contains a command ping to which Voca replies with "pong"
Register this command by adding following in cmds.py

**cmds.py**
```python
from commands import *
voca_commands={
	"ping":cmd_ping,
}
```

> *** Please note that this project is still in WIP status. ***

