#!/usr/bin/env python
# encoding: utf-8
"""
Enable pygtk to be used interacive by setting PyOS_InputHook.

Authors: Brian Granger
"""

#-----------------------------------------------------------------------------
#  Copyright (C) 2008-2009  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import sys
import gobject
from gi.repository import Gtk

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------


def _main_quit(*args, **kwargs):
    Gtk.main_quit()
    return False

def inputhook_gtk3():
    gobject.io_add_watch(sys.stdin, gobject.IO_IN, _main_quit)
    Gtk.main()
    return 0

