# sublime-profile
A simple sublime3 plugin, that makes synchronizing your Sublime Text 3 packages way easier.

This plugin is still under development, but if you want to, you can just clone the git to your Sublime-"Packages" folder and test it.

## How to use
1. Under Tools->sublime-profile click "upload profile" to upload your package-configuration and receive a profile id.
1. On a second machine, just click Tools->sublime-profile->"import profile", enter the profile id and restart sublime.
1. After the restart, all packages installed on the first machine will also be installed on the second one.
(depending on how many packages will be installed, this may take a while)

Note: Since the cloud node may need to be started, it could take a couple of seconds for the upload to finish. 

## Current features

- the "save" button anonymously uploads your "Package Control.sublime-settings" to a backup server and returns an identifier for your profile
- the "import" button asks you for your profile id, imports the uploaded json, backups your old "Package Control.sublime-settings" file to "Package Control.sublime-settings.backup" and overwrites it with the imported one. On the next restart, Package Control will automatically install all packages from the import, which you have are not installed yet.


## Possible future features
- full backup of all user-settings
- naming of the profile
- easier to remember identifier
