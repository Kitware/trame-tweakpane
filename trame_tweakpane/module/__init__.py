from pathlib import Path

serve_path = str(Path(__file__).with_name("serve").resolve())
serve = {"__trame_tweakpane": serve_path}
scripts = ["__trame_tweakpane/trame_tweakpane.umd.js"]
vue_use = ["trame_tweakpane"]
