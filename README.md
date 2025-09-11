![vy](vy.png) vy
================

A powerful modal editor written in python.

vy is a modal editor with a very modular architecture. 
Built on top of Tkinter (one of the most productive graphical toolkits), vy
has a great programming interface for plugins. Python is such an amazing language;
it turns vy such a powerful application because its plugin API is at a naturally high level.

Like emacs, vy allows simple mode creation. You can create modes that support programming languages and provide all kind of functionalities that varies from accessing irc or email checking.
The set of keys used in vy was carefully chosen to be handy although it is possible to make vy look like vim or emacs.

The syntax highlighting plugin is very minimalistic and extremely fast. It supports syntax highlighting 
for all languages that python-pygments supports. The source code of the syntax highlighting plugin is about 
120 lines of code. It is faster than the syntax highlighting plugins of both vim and emacs. :)
It is possible to easily implement new syntax highlighting themes that work for all languages because it uses
python pygments styles scheme.

There is a simple and consistent terminal-like plugin in vy that makes it possible to talk to external processes.
Such a feature is very handy when dealing with interpreters. One can just drop in pieces of code to an interpreter
then check the results. 

vy implements a Python debugger plugin and auto completion that permits debugging Python code easily and in a IDE like way. 
One can set break points, remove break points, run the code, see the cursor jumping to the line 
that is being executed, and much more.

It is possible to open multiple vertical/horizontal panes to edit different files. This makes it possible
to edit multiple files in a given tab. vy supports multiple tabs with a handy scheme of keys
to switch focus between tabs and panes. 

There is a vyrc file written in Python that is very well documented and organized to make it simple to load
plugins and set stuff at startup. You can take the best out of vy with no need to learn some odd language
like vimscript or Emacs Lisp; since vy is written in Python, you use Python to develop for it.

All built-in functions are well documented, which simplifies the process of plugin development as well as personalizing stuff.
The plugins are documented: the documentation can be accessed from vy by dropping Python code to the interpreter.

![screenshot-1](screenshot-1.jpg)

Features/Plugins
================

- **Python PDB Debugger**

- **Golang Delve Debugger**
    * https://github.com/go-delve/delve

- **GDB Debugger**

- **Nodejs inspect Debugger**

- **Rope Refactoring Tools**
    * https://github.com/python-rope/rope

- **Fuzzy Search**

- **Incremental Search**

- **Python Pyflakes Integration**
    * https://github.com/PyCQA/pyflakes

- **Tabs/Panes**

- **Self documenting**

- **HTML Tidy Integration**
    * http://tidy.sourceforge.net/

- **Powerful plugin API**

- **Syntax highlighting for 300+ languages**

- **Handy Shortcuts**

- **Ycmd/YouCompleteMe Auto Completion**
    * https://github.com/ycm-core/ycmd

- **Easily customizable (vyrc in python)**

- **Quick Snippet Search**

- **Smart Search with The Silver Searcher**
    * https://github.com/ggreer/the_silver_searcher

- **File Manager**

- **Python Static Type Checker**
    * http://mypy-lang.org/

- **Terminal-like**

- **Irc Client Plugin**
    * https://github.com/vyapp/vyirc

- **Find Function/Class Definition**

- **Python Vulture Integration**
    * https://github.com/jendrikseipp/vulture

- **Python Auto Completion**
    * https://github.com/davidhalter/jedi

- **Ruby Auto Completion**
    * https://github.com/vyapp/rsense

- **Golang Auto Completion**
    * https://github.com/nsf/gocode

- **Javascript Auto Completion**
    * https://github.com/nsf/gocode

Basic Install
=============

**Note:** 
vy requires Python3 to run, Python2 support is no longer available.

~~~
cd /tmp/
pip download vy
tar -zxvf vy-*
cd vy-*/
pip install -r requirements.txt
python setup.py install 
~~~

**Note:**
As vy is in development there may occur some changes to the vyrc file format, it is important to remove
your ~/.vy directory before a new installation in order to upgrade to a new version.

Documentation
=============

The vy docs may be outdated sometimes, i struggle to do my best to keep it all fine. There also
exists many features which weren't documented yet.

### [Vy Book](https://github.com/iogf/vy/wiki)

