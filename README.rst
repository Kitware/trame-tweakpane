===============
trame-tweakpane
===============

TweakPane widgets for trame made easy.

License
------------------------

trame-tweakpane is made available under the MIT License. For more details, see `LICENSE <https://raw.githubusercontent.com/Kitware/trame-tweakpane/master/LICENSE>`_. This license has been chosen to match the one used by `tweakpane <https://tweakpane.github.io/docs/>`_ which that project expose to trame.


Installation
------------------------

.. code-block:: console

    pip install trame-tweakpane


Usage
------------------------

.. code-block:: python

    from trame.widgets import tweakpane

    with layout:
        with tweakpane.Pane(title="Welcome", expanded=True, style="width: 200px;"):
            tweakpane.Binding(name="a", default=1, options="{ min: -6, max: 10, step: 0.2 }")
            with tweakpane.Folder(title="Sub-section"):
                tweakpane.Binding(name="b", default="Hello")
                tweakpane.BladeSeparator()
                tweakpane.Binding(name="c", default=0.465, options="{ label: 'Another number' }")
            with tweakpane.Tabs(pages="['First', 'Second', 'Third']"):
                with tweakpane.Tab(index=0):
                    tweakpane.Binding(name="d", default="something")
                with tweakpane.Tab(index=1):
                    tweakpane.Button(label="Click =>", title="Me", click=(print, "['clicked']"))
                with tweakpane.Tab(index=2):
                    tweakpane.Binding(name="f", default="something")

.. image:: https://raw.githubusercontent.com/Kitware/trame-tweakpane/master/examples/readme_example.png
  :width: 400
  :alt: Visual output of the code above

Development
------------------------

Build and install the Vue components

.. code-block:: console

    cd vue-components
    npm i
    npm run build
    cd -

Install the application

.. code-block:: console

    pip install -e .


