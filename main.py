import subprocess
from pathlib import Path
from colors import print_success, print_warning
import os

PATH = Path.home() / "goinfre/generateur_improba/"
GOINFRE_PATH = Path.home() / "goinfre/"

days = {
    "C03": ["strcmp", "strncmp", "strcat", "strncat", "strstr", "strlcat"]
}

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
    print(os.path.isdir(GOINFRE_PATH))
    if not os.path.isdir(GOINFRE_PATH):
        print_warning("Le GOINFRE n'est pas présent sur ce poste.")
    else:
        print("3 - C03")
        day_number = input("Selectionnez votre day :")
        while (days.get("C0" + day_number) is None):
            day_number = input("Selectionnez votre day :")
        run_git_clone()
        run_norminette()
        exercices = days.get("C0" + "3")
        from test_py.c03 import run_test
        run_test(PATH, exercices)


