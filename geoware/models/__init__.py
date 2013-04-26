import os
import re
import types

PACKAGE = 'geoware.models'
MODULE_RE = r"^.*.py$"
SKIP = ['.', '..', '__init__.py']

# Examine every file inside this module
submodules = []
module_dir = os.path.dirname( __file__)
for fname in os.listdir(module_dir):
    if fname not in SKIP and re.match(MODULE_RE, fname):
        module = __import__('{0}.{1}'.format(PACKAGE, fname[:-3]), {}, {}, fname[:-3])
        for name in dir(module):
            item = getattr(module, name)
            if isinstance(item, (type, types.ClassType)):
                # matched! include in module's namespace.
                exec '{0} = item'.format(name)
                submodules.append(name)

# Only reveals what each module allows us to see. Enforced by __all__ in each file
__all__ = submodules


