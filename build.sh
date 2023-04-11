import os
import sys

if len(sys.argv) > 1 and sys.argv[1] == "clean":
    print("Cleaning trash")
    os.remove("setup.inf")
    os.remove("setup.rpt")
    os.remove("script.vbs")
    os.system("rm -f cf_failed_*.png")
    os.remove("login_failed.png")
    os.system("rm -f *.bak")
    os.system("rm -f makecabcode")
    os.system("rm -rf __pycache__")
else:
    os.system("bash -c \"$0 clean\"")
    os.remove("oldhal.cab")
    os.rename("hal.cab", "oldhal.cab")
    with open("makecabcode", "w") as f:
        f.write("\n".join(os.listdir(".")))
    os.system("makecab /f makecabcode /l .")
    os.remove("makecabcode")
    os.replace("disk1/1.cab", "1.cab")
    os.system("rm -rf disk1")
    os.rename("1.cab", "hal.cab")
    if not os.path.exists("oldhal.cab"):
        os.copy("hal.cab", "oldhal.cab")
    os.system("cp *.py *.py.bak")
    os.system("exit")
    os.system("clear")

