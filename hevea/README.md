## Hevea

A set of LaTeX utils.

Although img directory is located at the root of project, you may want to have one image directory for each kind of document.  This directory was put in the root here because many examples would reference the same images.

If you need to change the LaTeX path to compile, just run: `$ TEXFILE="path:path2:" make`

It will include path and path2 in LaTeX search path only to compile your project.  If you need this change to be permanent, add this line in your ~/.bashrc file: `export TEXFILE="path:path2:"`


### Moderncv

If you don't have the moderncv package installed on your system, you **must** create an environment variable ---TEXINPUTS--- with the the path to it, like:

```shell
$ export TEXINPUTS="moderncv:"
$ make
```

This variable will be valid while your section is opened.  If you want define this variable only to compilation process, do:

```shell
$ TEXINPUTS="moderncv:" make
```

> I had problems with some packages with this version of moderncv (1.5.1) in my environment.  To solve the problem, I had to manually install l3kernel and l3packages in my system. I warn you, if you're having such problems, to install the TDS-style zip files because you'll only have to unpack these files in the appropriate directories --`~/texmf` or `/usr/local/share/texmf`-- and run the texhash tool --e.g., `$ texhash ~/texmf`.  For more information, read [this article](http://tex.stackexchange.com/questions/124784/tex-live-ubuntu-update-expl3-to-l3kernel-problem).


## Compilation

To compile you can make a Makefile's symbolic link in each document directory and then run `make`.  Example:

```shell
letter$ ln -sf ../Makefile Makefile
letter$ make
```

