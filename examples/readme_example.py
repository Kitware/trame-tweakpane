from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html
from trame_tweakpane.widgets import tweakpane


class DemoApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.ui = self._build_ui()

    def _build_ui(self):
        with DivLayout(self.server) as layout:
            layout.root.style = "width: 100vw; height: 100vh;"
            with html.Div(style="display: flex"), tweakpane.Pane(
                title="Welcome", expanded=True, style="width: 20rem;"
            ):
                tweakpane.Binding(
                    name="a",
                    default=1,
                    options="{ label: 'Nice name', min: -6, max: 10, step: 0.2 }",
                )
                with tweakpane.Folder(title="Sub-section"):
                    tweakpane.Binding(name="b", default="Hello")
                    tweakpane.BladeSeparator()
                    tweakpane.Binding(
                        name="c",
                        default=0.465,
                        options="{ label: 'Another number' }",
                    )
                with tweakpane.Tabs(pages="['First', 'Second', 'Third']"):
                    with tweakpane.Tab(index=0):
                        tweakpane.Binding(name="d", default="something")
                    with tweakpane.Tab(index=1):
                        tweakpane.Button(
                            label="Click =>",
                            title="Me",
                            click=(print, "['clicked']"),
                        )
                    with tweakpane.Tab(index=2):
                        tweakpane.Binding(name="f", default="something")
            return layout


def main():
    app = DemoApp()
    app.server.start()


if __name__ == "__main__":
    main()
