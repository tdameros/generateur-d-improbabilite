from cProfile import run
from re import I
import subprocess
from pathlib import Path
from colors import print_success, print_warning
import os
from test_py.c03 import run_test_c03
from test_py.c04 import run_test_c04

PATH = Path.home() / "goinfre/generateur_improba/"
GOINFRE_PATH = Path.home() / "goinfre/"

days = ["C03", "C04"]

def run_git_clone():
    subprocess.run(["rm", "-fr", PATH])
    subprocess.run(["clear"])
    url_repo = input("Entrer l'url du repo :")
    clone_process = subprocess.Popen(["git", "clone", url_repo, "generateur_improba"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=GOINFRE_PATH)
    clone_process.wait()
    while (clone_process.returncode != 0):
        url_repo = input("Entrer l'url du repo :")
        clone_process = subprocess.Popen(["git", "clone", url_repo, "generateur_improba"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=GOINFRE_PATH)
        clone_process.wait()


def run_norminette():
    norminette = subprocess.Popen(["norminette"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=PATH)
    norminette.wait()
    if (norminette.returncode == 1):
        print_warning("NORMINETTE ERROR !")
        out, err = norminette.communicate()
        print(out.decode())
    else:
        print_success("Norminette OK")


if __name__ == "__main__":
    subprocess.run(["clear"])
    print(os.path.isdir(GOINFRE_PATH))
    if not os.path.isdir(GOINFRE_PATH):
        print_warning("Le GOINFRE n'est pas présent sur ce poste.")
    else:
        print("3 - C03\n4 - C04")
        day_number = input("Selectionnez votre day :")
        while (str("C0" + day_number) not in days):
            day_number = input("Selectionnez votre day :")
        run_git_clone()
        run_norminette()
        if (str("C0" + day_number) == "C03"):
            run_test_c03(PATH)
        if (str("C0" + day_number) == "C04"):
            run_test_c04(PATH)