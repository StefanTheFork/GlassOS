import os

os.system("cls")

def init():
    print("""  
   _____ _                  ____   _____ 
  / ____| |                / __ \ / ____|
 | |  __| | __ _ ___ ___  | |  | | (___  
 | | |_ | |/ _` / __/ __| | |  | |\___ \ 
 | |__| | | (_| \__ \__ \ | |__| |____) |
  \_____|_|\__,_|___/___/  \____/|_____/   v0.2 github
            CrystalClearKERNEL
                                          """)
    import shell
    import commands
    import kernel
    
# for compiling (with pyinstaller), only compile this file (kernel.py) 