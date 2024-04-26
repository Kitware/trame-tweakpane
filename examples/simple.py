from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html
from trame_tweakpane.widgets import tweakpane


class DemoApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.ui = self._build_ui()

    def on_click(self):
        print("clicked")

    def blade_update(self, name, value):
        print("blade", name, value)

    def _build_ui(self):
        with DivLayout(self.server) as layout:
            layout.root.style = "width: 100vw; height: 100vh;"
            html.Div("Hello")
            with html.Div(style="display: flex"):
                with tweakpane.Pane(
                    title="Hello World",
                    expanded=True,
                    style="width: 300px;",
                ):
                    with tweakpane.Folder(title="Basic"):
                        tweakpane.Binding(
                            name="txt",
                            default="Hello world",
                        )
                        tweakpane.Binding(
                            name="number",
                            default=0.01,
                        )
                    with tweakpane.Folder(title="Sliders", expanded=True):
                        tweakpane.Binding(
                            name="slider",
                            default=0.123,
                            options="{ min: -1, max: 1 }",
                        )
                        tweakpane.Binding(
                            name="step",
                            default=0.05,
                            options="{ min: -1, max: 1 , step: 0.05 }",
                        )
                    with tweakpane.Folder(
                        title="Rest",
                        expanded=True,
                        disabled=("rest_disabled",),
                        hidden=("rest_hidden",),
                    ):
                        tweakpane.Binding(
                            name="list_number",
                            default=3,
                            options="{ label: 'List of Number', options: { a: 1, b: 2, c: 3 }}",
                        )
                        tweakpane.Binding(
                            name="list_string",
                            default="hello",
                            options="{ options: { none: '', something: 'hello', else: 'world' }}",
                        )
                        tweakpane.Binding(
                            name="bool",
                            default=True,
                        )
                        tweakpane.Binding(
                            name="color",
                            default={"r": 1 * 255, "g": 0, "b": 0.33 * 255},
                            options="{ view: 'color', picker: 'inline' }",
                        )
                        tweakpane.Binding(
                            name="point",
                            default={"x": 0, "y": 0},
                            options="{ picker: 'inline', expanded: true }",
                        )
                        tweakpane.Binding(
                            name="slider",
                            title="Graph",
                            options="{ readonly: true, view: 'graph', min: -1, max: +1 }",
                        )
                    tweakpane.Button(label="Label", title="Title", click=self.on_click)
                    with tweakpane.Tabs(pages="['First', 'Second', 'Blades']"):
                        with tweakpane.Tab(index=0):
                            tweakpane.Binding(
                                name="list_number",
                                options="{ label: 'List of Number', options: { a: 1, b: 2, c: 3 }}",
                            )
                            tweakpane.Binding(
                                name="list_string",
                                options="{ options: { none: '', something: 'hello', else: 'world' }}",
                            )
                        with tweakpane.Tab(index=1):
                            tweakpane.Binding(
                                name="slider", options="{ min: -1, max: 1 }"
                            )
                            tweakpane.Binding(
                                name="step", options="{ min: -1, max: 1 , step: 0.05 }"
                            )
                        with tweakpane.Tab(index=2):
                            tweakpane.BladeSlider(
                                label="Slider blade",
                                min=-10,
                                max=10,
                                value=-2,
                                change=(self.blade_update, "['slider', $event]"),
                            )
                            tweakpane.BladeSeparator()
                            tweakpane.BladeText(
                                label="Text blade",
                                value=-2,
                                format="(v) => v.toFixed(3)",
                                parse="(v) => Number(v)",
                                change=(self.blade_update, "['text', $event]"),
                            )
                            tweakpane.BladeList(
                                label="Text blade",
                                value=3,
                                options="{ a: 1, b: 2, c: 3 }",
                                change=(self.blade_update, "['list', $event]"),
                            )

                with html.Div(style="flex: 1; padding: 2rem;"):
                    html.Div("txt={{ txt }}")
                    html.Div("number={{ number }}")
                    html.Div("slider={{ slider }}")
                    html.Div("step={{ step }}")
                    html.Div("list_number={{ list_number }}")
                    html.Div("list_string={{ list_string }}")
                    html.Div("bool={{ bool }}")
                    html.Div("color={{ color }}")
                    html.Div("point={{ point }}")
                with html.Div(style="flex: 1; display: flex; flex-direction: column;"):
                    html.Input(v_model="txt")
                    html.Input(v_model="slider", min=-1, max=1, type="range")
                    html.Input(v_model="step", step=0.05, min=-1, max=1, type="range")
                    html.Input(type="checkbox", v_model="bool")

                    with html.Div():
                        html.Span("Disable/Hidden Rest")
                        html.Input(type="checkbox", v_model=("rest_disabled", False))
                        html.Input(type="checkbox", v_model=("rest_hidden", False))

            return layout


def main():
    app = DemoApp()
    app.server.start()


if __name__ == "__main__":
    main()
