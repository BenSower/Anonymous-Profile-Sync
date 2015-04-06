# sublime-profile
A simple sublime3 plugin, that lets you upload a list of your installed packages and import and install them based on your backup.


This plugin is still under development, but if you want to, you can just clone the git to your Sublime-"Packages" folder and test it.

Current features:

- the "save" button automatically uploads your "Package Control.sublime-settings" to a small heroku app and returns an anonymous id
- the "import" button asks you for the id you got from the upload, imports the related json and prints the list of uploaded modules.
