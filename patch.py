import os
import shutil
import patcher

PATH = os.path.dirname(__file__)
ccmd_patch = os.path.join(PATH, "patch.diff")
ccmd_orig = os.path.join(PATH, "python-customcmd", "customcmd")
ccmd_orig_dest = os.path.join(PATH, "customcmd-original")
ccmd_out = os.path.join(PATH, "customcmd-patch")

def main():
    if os.path.exists(ccmd_out):
        shutil.rmtree(ccmd_out)
    shutil.copytree(ccmd_orig, ccmd_out, dirs_exist_ok=True)
    patch = patcher.fromfile(ccmd_patch, debugmode=True)
    patch.apply(root=PATH)

if __name__ == "__main__":
    main()