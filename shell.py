import kernel
import commands

kernel.init()

while True:
    line = input(" admin > ")

    if line == "write":
        commands.write()

    if line == "opentext":
        commands.opentext()

    if line == "clock":
        commands.clock()

    if line == "shutdown":
        commands.shutdown()

    if line == "help":
        commands.help()