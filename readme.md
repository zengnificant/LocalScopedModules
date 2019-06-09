LocalScopedModules
=================

About
------------------
This is a Sublime Text 3 plugin to auto complete path for projects using [babel-plugin-local-scoped-modules](https://github.com/zengnificant/babel-plugin-local-scoped-modules).


Installation
------------------

**firstly:**
```shell
git clone git@github.com:zengnificant/LocalScopedModules.git
```

**then:**

  Open sublime text -> Preferences -> Browser Packages -> put the downloaded `LocalScopedModules` dir  in the `packages` dir.



Usage
-----------------

Set up a config file  `LocalScopedModules.sublime-settings` in the sublime's `packages/User` dir. Follow  [default config file](https://github.com/zengnificant/LocalScopedModules/blob/master/LocalScopedModules.sublime-settings). and  Config for your projects. Then it's working!




Patch for AutoFileName:
------------------------
If you are using AutoFileName plugin, you may find both `AutoFileName` and this plugin working and they become annoying...

So I made [a patch](https://github.com/zengnificant/patch/blob/master/autofilename/autofilename.py) for  `AutoFileName`.

Procedure:

1.  Open sublime text -> Preferences -> Browser Packages ->`Installed Packages`
->rename the `AutoFileName.sublime-package` as  `AutoFileName.zip` ->
->unzip `AutoFileName.zip`  and remove the file of `package-metadata.json` (if not it'll be automaticly deleted by sublime).

2. from  Step 1,you got the `AutoFileName` package, replace the default in the   `AutoFileName` package with [the patch](https://github.com/zengnificant/patch/blob/master/autofilename/autofilename.py). Then put the `AutoFileName` package to sublime's `Packages` dir.



Lisense
--------------
MIT














