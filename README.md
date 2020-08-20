# pyZomboid

A python api for reading (and executing) lua files from TheIndieStone's Project Zomboid.

*please note this emulation is a total WIP and very incomplete*

pyZomboid uses the python module lupa to execute lua, giving full access to PZ's lua tables
and functions. PZ's java component is emulated in python and additional lua.

The goal is not simulate the playable parts of PZ, but the ability to load, test and debug various lua
components and mods from custom test scripts, or a shell interface.

Some aspects of the code are direct ports of the original java, to ensure files are loaded and parsed
identical to PZ, and to ensure it interfaces with the lua correctly.  
Due to having to match PZ's API, classes and code exposed to the lua will fall well outside python standards 
for naming conventions. Also for exposed variables and class attributes the standard python list/dict are 
generally replaced with ArrayList and HashMap classes that act as proxies.
