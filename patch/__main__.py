import os
import shutil
from . import patch

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ccmd_patch = os.path.join(PATH, "patch.diff")
ccmd_orig = os.path.join(PATH, "python-customcmd", "customcmd")
ccmd_orig_dest = os.path.join(PATH, "customcmd-original")
ccmd_out = os.path.join(PATH, "customcmd-patch")

def main():
    if os.path.exists(ccmd_out):
        shutil.rmtree(ccmd_out)
    shutil.copytree(ccmd_orig, ccmd_out, dirs_exist_ok=True)
    patch.setdebug()
    patcher = patch.fromfile(ccmd_patch)
    patcher.apply(root=PATH)

if __name__ == "__main__":
    main()