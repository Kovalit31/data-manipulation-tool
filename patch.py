import os
import shutil

PATH = os.path.dirname(__file__)
ccmd_patches_dir = os.path.join(PATH, "ccmd_patches")
ccmd_orig = os.path.join(PATH, "python-customcmd", 'customcmd')
patched = os.path.join(PATH, "python-ccmd-patched")

def main() -> None:
    content_of_ccmd_patches = []
    os.chdir(ccmd_patches_dir)
    for root, _, files in os.walk("."):
        for x in range(len(files)):
            content_of_ccmd_patches.append(os.path.join(root, files[x]))
    os.chdir(PATH)
    shutil.copytree(ccmd_orig, patched, dirs_exist_ok=True)
    os.chdir(patched)
    for x in range(len(content_of_ccmd_patches)):
        if os.path.exists(content_of_ccmd_patches[x]):
            patched_data = readlines(os.path.join(ccmd_patches_dir, content_of_ccmd_patches[x]))
            data = readlines(content_of_ccmd_patches[x])
            if data != None:
                to_wr = patch(patched_data, data)
                write(to_wr, content_of_ccmd_patches[x])
            else:
                print("Can't patch", content_of_ccmd_patches[x])
        else:
            shutil.copyfile(os.path.join(ccmd_patches_dir, content_of_ccmd_patches[x]), content_of_ccmd_patches[x])

def readlines(_path: str) -> list:
    _ret = []
    try:
        file = open(_path, 'r', encoding='utf-8')
        _ret = file.readlines()
        file.close()
    except:
        return _ret

def patch(_patch_data: list, _orig_file: list) -> list:
    # add_act = False
    # index = 0
    # file_end = False
    # patched = []
    # if _patch_data == None or _orig_file == None:
    #     return None
    # for x in range(len(_patch_data)):
    #     if _patch_data[x].startswith("#"+"+"*12):
    #         print("It need to start adding!")
    #         add_act = True
    #         continue
    #     if _patch_data[x].startswith("#"+"="*12):
    #         print("Stop patching!")
    #         add_act = False
    #         continue
    #     if not add_act and not file_end:
    #         for y in range(len(_orig_file)):
    #             z = y + index
    #             patched.append(_orig_file[z])
    #             if z >= len(_orig_file):
    #                 file_end = True
    #                 break
    #             if _orig_file[z] == _patch_data[x]:
    #                 index = z
    #                 break
    #     elif not add_act and not file_end:
    #         print("It seems, that you can't patch file!")
    #         return
    #     elif add_act and not file_end:
    #         patched.append(_patch_data[x])
    #     else:
    #         patched.append(_patch_data[x])
    pass
                

def write(_path: str, _data: list) -> None:
    try:
        file = open(_path, 'w', encoding='utf-8')
        file.write("".join(_data))
        file.close()
    except:
        return

if __name__ == "__main__":
    main()