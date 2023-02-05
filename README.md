# vehiclemeta-formatter
A CLI tool for correcting paths in fxmanifest.lua files of the output of the tool called "rpf2fivem". Thanks Avenze for creating "rpf2fivem" making converting vehicles this easy.

## How to use it?

First of all you need to have Python 3 installed on your system to run this tool.

I would suggest you to collect all the vehicles you want to use in a folder and let this tool go through all the sub directories, finds and fixes the meta file paths in fxmanifest.lua's. So the folder structure should be like this: 

```
[vehiclepack]
│
└───car1
│   │   fxmanifest.lua
│   │
│   └───data
│       │   ...
│   │
│   └───stream
│       │   ...
│   
└───car2
│   │   fxmanifest.lua
│   │
│   └───data
│       │   ...
│   │
│   └───stream
│       │   ...
```

If your vehicle pack looks like this, just run this command:
```
python vehiclemeta-formatter.py
```

When the tool prompts you to enter the full path for the vehicle pack please enter the FULL PATH. For example: 'C\FXServer\resources\vehiclepack'
