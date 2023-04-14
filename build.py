import os, sys, shutil
platform_functions = {
    'win32': (
        lambda: shutil.rmtree('Linux', ignore_errors=True),
        lambda: shutil.copytree('Windows', '.', dirs_exist_ok=True)
    ),
    'Linux': (
        lambda: shutil.rmtree('Windows', ignore_errors=True),
        lambda: shutil.copytree('Linux', '.', dirs_exist_ok=True)
    )
}

delete_function, copy_function = platform_functions.get(sys.platform, (None, None))
if delete_function is not None:
    delete_function()
if copy_function is not None:
    copy_function()