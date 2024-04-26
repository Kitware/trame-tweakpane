from trame_client.widgets.core import AbstractElement

from trame_tweakpane import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


__all__ = [
    "Pane",
    "Binding",
    "Folder",
    "Button",
    "Tabs",
    "Tab",
    "BladeSlider",
    "BladeText",
    "BladeList",
]


class Pane(HtmlElement):
    """
    Main container for panel.

    Args:
    ----
        title (str): Panel title shown at the top that let you toggle its content.
        expanded (bool): Should you start with the panel open or closed. Default is closed.

    Events:
        created: triggered when the object get created.
        change: triggered when any child elem is getting changed with the event of the modification.
        deleted: triggered when the object get deleted.
        export: triggered with the exported state when the method export_state() is called

    """

    _next_id = 0

    def __init__(self, **kwargs):
        super().__init__(
            "tp-pane",
            **kwargs,
        )
        self._attr_names += [
            "expanded",
            "title",
        ]
        self._event_names += [
            "created",
            "deleted",
            "change",
            "export",
        ]
        Pane._next_id += 1
        self.__ref = kwargs.get("ref", f"Pane_{Pane._next_id}")
        self._attributes["ref"] = f'ref="{self.__ref}"'

    def import_state(self, state_to_load):
        """Load provided state into the full Pane."""
        self.server.js_call(self.__ref, "importState", state_to_load)

    def export_state(self):
        """Trigger a state export that will result in the "export" event to happen."""
        self.server.js_call(self.__ref, "exportState")


class Binding(HtmlElement):
    """
    Generate a Binding Blade.

    Args:
    ----
        name (string): Name of the state variable to control.
        default (python value): Value to initialize the state variable with.
        options (string): JS object capturing the binding options (view, min, max, ...).

    Events:
        change: Triggered when user interact with the UI and change the variable.
                But regular reactive state management will also work naturally.

    """

    def __init__(self, default=None, **kwargs):
        super().__init__(
            "tp-binding",
            **kwargs,
        )
        self._attr_names += [
            "name",
            ("options", ":options"),
        ]
        self._event_names += [
            "change",
        ]
        self.server.state.setdefault(kwargs.get("name"), default)


class Folder(HtmlElement):
    """
    Create a grouping structure that can be collapsed or expanded dynamically or even hidden dynamically.

    Args:
    ----
        title (str): Label to display for that group panel.
        expanded (bool): Start closed by default but if set to True, it will be expanded.
        hidden (bool): Reactive property that let you hide its full content if set to true.
        disabled (bool): Reactive property that let you disable edits when set to true.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-folder",
            **kwargs,
        )
        self._attr_names += [
            "expanded",
            "title",
            "hidden",
            "disabled",
        ]


class Button(HtmlElement):
    """
    Create a Button element.

    Args:
    ----
        label (str): Text you want to see on the left.
        title (str): Text you want to see in the button.

    Events:
        click (fn): Function or method you want to call when the button is clicked.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-button",
            **kwargs,
        )
        self._attr_names += [
            "label",
            "title",
        ]
        self._event_names += [
            "click",
        ]


class Tabs(HtmlElement):
    """
    Tabs container.

    Args:
    ----
        pages (str): List of label you want for your pages (pages="['first', 'second']")
        hidden (bool): Reactive property that let you hide its full content if set to true.
        disabled (bool): Reactive property that let you disable edits when set to true.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-tabs",
            **kwargs,
        )
        self._attr_names += [
            "hidden",
            "disabled",
            ("pages", ":pages"),
        ]


class Tab(HtmlElement):
    """
    Define the content of a given Tab.

    Args:
    ----
        index (int): Must provide the index of the tab to link to. Start at 0.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-tab",
            **kwargs,
        )
        self._attr_names += [
            "index",
        ]


class BladeSlider(HtmlElement):
    """
    Blade with 'slider' as view.

    Args:
    ----
        label (str): Label to use for blade.
        hidden (bool): Reactive property that let you hide its full content if set to true.
        disabled (bool): Reactive property that let you disable edits when set to true.
        min (number): Minimum value for the slider.
        max (number): Maximum value for the slider.
        step (number): Step side for the slider.
        value (number): Initial value to start with.
        format (str): JavaScript function processing the value so it can be displayed to the UI.

    Events:
        change: triggered when user interact with the UI.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-bladeslider",
            **kwargs,
        )
        self._attr_names += [
            "hidden",
            "disabled",
            "label",
            ("min", ":min"),
            ("max", ":max"),
            ("step", ":step"),
            ("value", ":value"),
            ("format", ":format"),
        ]
        self._event_names += [
            "change",
        ]


class BladeText(HtmlElement):
    """
    Blade with 'text' as view.

    Args:
    ----
        label (str): Label to use for blade.
        hidden (bool): Reactive property that let you hide its full content if set to true.
        disabled (bool): Reactive property that let you disable edits when set to true.
        value (number): Initial value to start with.
        parse (str): JavaScript function parsing the user input.
        format (str): JavaScript function processing the value so it can be displayed to the UI.

    Events:
        change: triggered when user interact with the UI.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-bladetext",
            **kwargs,
        )
        self._attr_names += [
            "hidden",
            "disabled",
            "label",
            ("value", ":value"),
            ("format", ":format"),
            ("parse", ":parse"),
        ]
        self._event_names += [
            "change",
        ]


class BladeList(HtmlElement):
    """
    Blade with 'list' as view.

    Args:
    ----
        label (str): Label to use for blade.
        hidden (bool): Reactive property that let you hide its full content if set to true.
        disabled (bool): Reactive property that let you disable edits when set to true.
        value (number): Initial value to start with.
        options (str): JavaScript list of available options.

    Events:
        change: triggered when user interact with the UI.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-bladelist",
            **kwargs,
        )
        self._attr_names += [
            "hidden",
            "disabled",
            "label",
            ("value", ":value"),
            ("options", ":options"),
        ]
        self._event_names += [
            "change",
        ]


class BladeSeparator(HtmlElement):
    """
    Separator Blade to create some spacing.

    Args:
    ----
        hidden (bool): Reactive property that let you hide its full content if set to true.
        disabled (bool): Reactive property that let you disable edits when set to true.

    """

    def __init__(self, **kwargs):
        super().__init__(
            "tp-bladeseparator",
            **kwargs,
        )
        self._attr_names += [
            "hidden",
            "disabled",
        ]
