"""
Overview
========

This plugin does autocompletion using jedi library.


Usage
=====

Whenever one presses <Control-Key-period> in INSERT mode
it should popup a window with possible completions.


Key-Commands
============

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.

"""

from vyapp.complete import CompleteWindow
from jedi import Script
import sys

class PythonCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        line        = area.indcur()[0]
        size        = len(area.get('insert linestart', 'insert'))
        script      = Script(source, line, size, area.filename)
        completions = script.completions()

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)
        self.bind('<F1>', lambda event: sys.stdout.write('%s\n%s\n' % ('#' * 80, self.box.elem_desc())))
        # area.wait_window(self)

def install(area):
    trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                        lambda event: PythonCompleteWindow(event.widget), add=False)
    area.install((-1, '<<Load-text/x-python>>', trigger), (-1, '<<Save-text/x-python>>', trigger),
                 (-1, '<<LoadData>>', lambda event: area.unhook('INSERT', '<Control-Key-period>')))



