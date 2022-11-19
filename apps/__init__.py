from glob import glob
from pathlib import Path
from importlib import import_module

base_path = Path(__file__).parent
_apps = glob('*.py', root_dir=base_path)
apps = []
for app in _apps:
    if app not in ['__init__.py', 'BaseApp.py']:
        app = app[:-3]
        app_import = import_module('apps.'+app)
        app_class = getattr(app_import, app)
        apps.append(app_class)
