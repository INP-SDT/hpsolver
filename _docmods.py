# -*- coding: utf-8 -*-
"""Documentation maker — modules.
"""
import docspyer
import hpsolver

DOCPATH = 'docs/sources'

MODULES = [
    hpsolver.sem,
    hpsolver.hps,
    hpsolver.polys
]

config = {
    'docsname': 'hpsolver',
    'hostname': 'hpsolver',
    'modrefs': True,
    'clsverbs': 2
}

docspyer.docmods(
    MODULES, DOCPATH, **config
)
