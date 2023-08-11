# -*- coding: utf-8 -*-
# This file is part of MyPaint.
# Copyright (C) 2007-2015 by Martin Renold <martinxyz@gmx.ch>
# Copyright (C) 2015-2016 by the MyPaint Development Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.


"""Program meta-information: consts & display.

See also `lib.meta`.

"""


## Imports
from __future__ import division, print_function

import sys
import os
import platform

from gi.repository import Gtk
from gi.repository import GdkPixbuf
from gi.repository import GLib
import cairo

from lib.gettext import C_
import lib.meta
from lib.xml import escape


## Program-related string constants

COPYRIGHT_STRING = C_(
    "About dialog: copyright statement",
    u"Copyright (C) 2005-2017\n"
    u"Martin Renold and the MyPaint Development Team"
)
WEBSITE_URI = "http://mypaint.org"
LICENSE_SUMMARY = C_(
    "About dialog: license summary",
    u"This program is free software; you can redistribute it and/or modify "
    u"it under the terms of the GNU General Public License as published by "
    u"the Free Software Foundation; either version 2 of the License, or "
    u"(at your option) any later version.\n"
    u"\n"
    u"This program is distributed in the hope that it will be useful, "
    u"but WITHOUT ANY WARRANTY. See the COPYING file for more details."
)

## Credits-related string constants

# Strings for specific tasks, all translated

_TASK_PROGRAMMING = C_(
    "About dialog: credits: tasks",
    u"programming"
)
_TASK_PORTING = C_(
    "About dialog: credits: tasks",
    u"portability"
)
_TASK_PROJECT_MANAGEMENT = C_(
    "About dialog: credits: tasks",
    u"project management"
)
_TASK_BRUSHES = C_(
    "About dialog: credits: tasks: brush presets and icons",
    u"brushes"
)
_TASK_PATTERNS = C_(
    "About dialog: credits: tasks: background paper textures",
    u"patterns"
)
_TASK_TOOL_ICONS = C_(
    "About dialog: credits: tasks: icons for internal tools",
    u"tool icons"
)
_TASK_APP_ICON = C_(
    "About dialog: credits: tasks: the main application icon",
    u"desktop icon"
)
_TASK_PALETTES = C_(
    "About dialog: credits: tasks: palettes",
    u"palettes"
)

_TASK_DOCS = C_(
    "About dialog: credits: tasks: docs, manuals and HOWTOs",
    u"documentation"
)
_TASK_SUPPORT = C_(
    "About dialog: credits: tasks: user support",
    u"support"
)
_TASK_OUTREACH = C_(
    "About dialog: credits: tasks: outreach (social media, ads?)",
    u"outreach"
)
_TASK_COMMUNITY = C_(
    "About dialog: credits: tasks: running or building a community",
    u"community"
)

_TASK_COMMA = C_(
    "About dialog: credits: tasks: joiner punctuation",
    u", ",
)

# List contributors in order of their appearance.
# The author's name is always written in their native script,
# and is not marked for translation. It may also have:
# transcriptions (Latin, English-ish) in brackets following, and/or
# a quoted ’nym in Latin script.
# For <given(s)> <surname(s)> combinations,
# a quoted publicly-known alias may go after the given name.

# TODO: Simplify/unify how the dialog is built.
#  - This should really be built from a giant matrix.
#  - Each task type should determine a tab of the about dialog
#  - Contributors will still appear on multiple tabs,
#     - but that'd be automatic now
#  - Keep it reasonably simple, so that contributors can add themselves!
#  - Maybe get rid of the (%s) formatting junk?
#  - Split out ’nyms and transliterations too?

_AUTHOR_CREDITS = [
    f"Martin Renold ({_TASK_PROGRAMMING})",
    f"Yves Combe ({_TASK_PORTING})",
    f"Popolon ({_TASK_PROGRAMMING})",
    f"Clement Skau ({_TASK_PROGRAMMING})",
    f"Jon Nordby ({_TASK_PROGRAMMING})",
    f"Álinson Santos ({_TASK_PROGRAMMING})",
    f"Tumagonx ({_TASK_PORTING})",
    f"Ilya Portnov ({_TASK_PROGRAMMING})",
    f"Jonas Wagner ({_TASK_PROGRAMMING})",
    f"Luka Čehovin ({_TASK_PROGRAMMING})",
    u"Andrew Chadwick (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_PROGRAMMING,
            _TASK_PROJECT_MANAGEMENT,
            _TASK_PORTING,
        ]
    ),
    f"Till Hartmann ({_TASK_PROGRAMMING})",
    f'David Grundberg ({_TASK_PROGRAMMING})',
    f"Krzysztof Pasek ({_TASK_PROGRAMMING})",
    f"Ben O’Steen ({_TASK_PROGRAMMING})",
    f"Ferry Jérémie ({_TASK_PROGRAMMING})",
    f"しげっち ‘sigetch’ ({_TASK_PROGRAMMING})",
    f"Richard Jones ({_TASK_PROGRAMMING})",
    f"David Gowers ({_TASK_PROGRAMMING})",
    f"Micael Dias ({_TASK_PROGRAMMING})",
    u"Anna Harren (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_COMMUNITY,
            _TASK_PROGRAMMING,
            _TASK_DOCS,
        ]
    ),
    f"Sebastien Leon ({_TASK_PROGRAMMING})",
    f"Ali Lown ({_TASK_PROGRAMMING})",
    f"Brien Dieterle ({_TASK_PROGRAMMING})",
    f"Jenny Wong ({_TASK_PROGRAMMING})",
    f"Dmitry Utkin ‘loentar’ ({_TASK_PROGRAMMING})",
    f"ShadowKyogre ({_TASK_PROGRAMMING})",
    u"Albert Westra (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_COMMUNITY,
            _TASK_PROGRAMMING,
        ]
    ),
    f"Cortexer ({_TASK_PROGRAMMING})",
    f"Elliott Sales de Andrade ({_TASK_PORTING})",
    f"Alberto Leiva Popper ({_TASK_PROGRAMMING})",
    f"Alinson Xavier ({_TASK_PROGRAMMING})",
]
_ARTIST_CREDITS = [
    f"Artis Rozentāls ({_TASK_BRUSHES})",
    f"Popolon ({_TASK_BRUSHES})",
    u"Marcelo ‘Tanda’ Cerviño (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_PATTERNS,
            _TASK_BRUSHES,
        ]
    ),
    u"David Revoy (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_BRUSHES,
            _TASK_TOOL_ICONS,
            _TASK_OUTREACH,
        ]
    ),
    u"Ramón Miranda (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_BRUSHES,
            _TASK_PATTERNS,
        ]
    ),
    f"Enrico Guarnieri ‘Ico_dY’ ({_TASK_BRUSHES})",
    f'Sebastian Kraft ({_TASK_APP_ICON})',
    f"Nicola Lunghi ({_TASK_PATTERNS})",
    f"Toni Kasurinen ({_TASK_BRUSHES})",
    f"Сан Саныч ‘MrMamurk’ ({_TASK_PATTERNS})",
    f"Andrew Chadwick ({_TASK_TOOL_ICONS})",
    f"Ben O’Steen ({_TASK_TOOL_ICONS})",
    f"Guillaume Loussarévian ‘Kaerhon’ ({_TASK_BRUSHES})",
    u"Jakub Steiner ‘jimmac’ (%s)"
    % _TASK_COMMA.join(
        [
            _TASK_APP_ICON,
            _TASK_PALETTES,
        ]
    ),
    f"ShadowKyogre ({_TASK_TOOL_ICONS})",
    f"Albert Westra ({_TASK_TOOL_ICONS})",
]
_TRANSLATOR_CREDITS = C_(
    "About dialog: credits: translator credits (your name(s) here!)",
    u"translator-credits",
)


## About dialog for the app

def get_libs_version_string():
    """Get a string describing the versions of important libs.

    >>> type(get_libs_version_string()) == str
    True

    """
    versions = [
        ("Python", "{major}.{minor}.{micro}".format(
            major = sys.version_info.major,
            minor = sys.version_info.minor,
            micro = sys.version_info.micro,
        )),
        ("GTK", "{major}.{minor}.{micro}".format(
            major = Gtk.get_major_version(),
            minor = Gtk.get_minor_version(),
            micro = Gtk.get_micro_version(),
        )),
        ("GdkPixbuf", GdkPixbuf.PIXBUF_VERSION),
        ("Cairo", cairo.cairo_version_string()),  # NOT cairo.version
        ("GLib", "{major}.{minor}.{micro}".format(
            major = GLib.MAJOR_VERSION,
            minor = GLib.MINOR_VERSION,
            micro = GLib.MICRO_VERSION,
        )),
    ]
    return ", ".join([" ".join(t) for t in versions])


def run_about_dialog(mainwin, app):
    """Runs MyPaint's about window as a transient modal dialog."""
    d = Gtk.AboutDialog()
    d.set_transient_for(mainwin)
    d.set_program_name(lib.meta.MYPAINT_PROGRAM_NAME)
    p = escape(lib.meta.MYPAINT_PROGRAM_NAME)
    v_raw = app.version or lib.meta.MYPAINT_VERSION
    v = "{mypaint_version}\n\n<small>({libs_versions})</small>".format(
        mypaint_version = escape(v_raw),
        libs_versions = escape(get_libs_version_string()),
    )
    if os.name == "nt":
        # The architecture matters more on windows, to the extent that
        # we release two separate builds with differing names.
        bits_str, linkage = platform.architecture()
        bits_str = {
            "32bit": "w32",
            "64bit": "w64",
        }.get(bits_str, bits_str)
        p = "{progname} {w_bits}".format(
            progname = escape(lib.meta.MYPAINT_PROGRAM_NAME),
            w_bits = escape(bits_str),
        )
    d.set_program_name(p)
    d.set_version(v)
    d.set_copyright(escape(COPYRIGHT_STRING))
    d.set_website(WEBSITE_URI)
    d.set_logo(app.pixmaps.mypaint_logo)
    d.set_license(LICENSE_SUMMARY)
    d.set_wrap_license(True)
    d.set_authors(_AUTHOR_CREDITS)
    d.set_artists(_ARTIST_CREDITS)
    d.set_translator_credits(_TRANSLATOR_CREDITS)
    d.run()
    d.destroy()
