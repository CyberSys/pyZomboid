# pyZomboid

A python api for reading (and executing) lua files from TheIndieStone's Project Zomboid.

pyZomboid uses the python module lupa to execute lua, giving full access to PZ's lua tables
and functions. PZ's java component is emulated in python and additional lua.

The goal is not to have a PZ simulator, but the ability to load, test and debug various lua
components and mods from custom test scripts, or a shell interface.

*please note this emulation is a total WIP and very incomplete*

PZ's exposed java api is vast. Currently the only simulated classes and methods are
what was required to load all files without issue, and trigger the initial events
OnLoadSoundBanks up to OnPostDistributionMerge *(as well as load ORGM)*

Be aware this is a total hackjob, incomplete, undocumented, and used in the creation of
the ORGM discord bot. Don't expect it to give you anything but headaches in its current
state unless you hit it with a very large hammer.

If you encounter this error:

`lupa._lupa.LuaError: ./server/MetalDrum/SMetalDrumSystem.lua:8: module 'MetalDrum/BuildingObjects/ISMetalDrum.lua' not found`

line 8 of server/MetalDrum/SMetalDrumSystem.lua needs to be editted (remove the ".lua" part from the require statement)
