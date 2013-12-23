SsschemeToggle
==============

Sublime Text plugin to switch global color scheme between two states.

Usage:
    Edit your Preferences > Key Bindings - User file to include the following lines:
      
    {
        "keys": ["f12"], 
        "command": "toggle_color_scheme",
        "args":
        {
            "color_scheme_1": "Packages/Color Scheme - Default/Dawn.tmTheme" ,
            "color_scheme_2": "Packages/Color Scheme - Default/Monokai.tmTheme"
        }
    }

Replacing "keys" with your desired hotkey and the "color_scheme_X" fields with your desired color schemes.

Credit for the bulk of this code goes to Riccardo Marotti (http://stackoverflow.com/questions/13121687/keyboard-shortcut-to-change-color-scheme-in-sublime-text-2/20511059#20511059)
