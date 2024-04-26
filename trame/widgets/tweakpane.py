from trame_tweakpane.widgets.tweakpane import *


def initialize(server):
    from trame_tweakpane import module

    server.enable_module(module)
