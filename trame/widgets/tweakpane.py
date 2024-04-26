from trame_tweakpane.widgets.tweakpane import *  # noqa: F403


def initialize(server):
    from trame_tweakpane import module

    server.enable_module(module)
