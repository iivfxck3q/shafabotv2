import importlib.util
import sys

library_path = 'library/hook.py'

spec = importlib.util.spec_from_file_location("hook", library_path)
hook = importlib.util.module_from_spec(spec)
sys.modules["hook"] = hook
spec.loader.exec_module(hook)

hook.main()