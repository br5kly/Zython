import os

os.system("pip install tqdm")
os.system('pip install rich')
os.system('pip install requests')
os.system('pip install cython')
os.system('pip install bs4')
os.system('pip install setuptools')


def clear():
    os.system('clear')


def setup():
    if os.path.exists('/data/data/com.termux/files/home/.termux/'):
        print("\033[1;32m YOUR SYSTEM IS TERMUX")
        if os.path.exists('/data/data/com.termux/files/home/.termux/font.ttf'):
            if os.path.getsize('/data/data/com.termux/files/home/.termux/font.ttf') == 778284:
                pass
            else:
                os.system('mv font.ttf /data/data/com.termux/files/home/.termux/font.ttf')
                os.system('termux-reload-settings')
        else:
            os.system('mv font.ttf /data/data/com.termux/files/home/.termux/font.ttf')
            os.system('termux-reload-settings')
    else:
        print("\033[1;31m Run On Termux Only")
        exit()

    import time

    from rich.progress import Progress

    with Progress() as progress:
        task1 = progress.add_task("[green]تنــزيل متطلبات ...", total=100)
        task2 = progress.add_task("[green]تثبيت ملف لغة عـربية...", total=20)
        task3 = progress.add_task("[green]تحقق من تحديثات...", total=20)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            progress.update(task2, advance=0.3)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
    clear()


setup()


class Cython_Install:
    def __init__(self):

        self.opt = "/data/data/com.termux/files/usr/opt"
        self.bin = "/data/data/com.termux/files/usr/bin"
        self.execute = self.opt + "/zython.py"
        self.run = self.bin + "/ZYTHON"
        self.cython = "Zython_So.cpython-311.so"
        if not os.path.exists(self.opt):
            os.system(f"mkdir {self.opt}")
        if os.path.exists("zython.py"):
            os.system(f"mv zython.py {self.opt}")
        if os.path.exists(self.cython):
            os.system(f"mv {self.cython} {self.opt}")
        else:
            exit("مثبت بالفعل !")
        with open(self.run, 'w') as file:
            file.write(f'''
#!/bin/bash

# Check if exactly one argument is provided
if [ $# -ne 1 ]; then
    echo "يرجى وضع اسم ملف بايثون للبدء"
    exit 1
fi


argument=$1

python {self.execute} $argument         
''')
        os.system(f"chmod +x {self.run}")
        print("\033[2;32m \n \n تم التثبيت بنجاح يمكنك الاستخدام بواسطة امر ZYTHON")


Cython_Install()
