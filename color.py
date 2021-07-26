import os
import time
###################
# Codado por Zoro #
###################

#Cores
Ve = '\033[1;31m' #Vermelho
Vd = '\033[1;32m' #Verde
Am = '\033[1;33m' #Amarelo
Az = '\033[1;34m' #Azul
Br = '\033[1;37m' #Branco

os.system("clear")

os.system("pkg install figlet")
os.system("clear")
print("\033[1;31m")
os.system("figlet Color")

print("""\033[1;32m
 Cores: \n\n
l============l
l "Verde"    l
l "Amarelo"  l
l "Vermelho" l
l "Azul"     l
l============l
""")
cor = input(">>> ")

if cor == "Verde":
    os.chdir('/data/data/com.termux/files/home/Color/Bash/')
    os.system('cp Verde /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/usr/etc/')
    os.system('rm -rf bash.bashrc')
    os.system('mv Verde bash.bashrc')
    print(f'{Vd}Pronto! \n\n')
    print('Para salvar use o comando "exit" e volte ao terminal.')
elif cor == "Amarelo":
    os.chdir('/data/data/com.termux/files/home/Color/Bash/')
    os.system('cp Amarelo /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/usr/etc/')
    os.system('rm -rf bash.bashrc')
    os.system('mv Amarelo bash.bashrc')
    print(f'\n{Vd}Pronto! \n\n')
    print('Para salvar use o comando "exit" e volte ao terminal.')
elif cor == "Vermelho":
    os.chdir('/data/data/com.termux/files/home/Color/Bash/')
    os.system('cp Vermelho /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/usr/etc/')
    os.system('rm -rf bash.bashrc')
    os.system('mv Vermelho bash.bashrc')
    print(f'{Vd}Pronto! \n\n')
    print('Para salvar use o comando "exit" e volte ao terminal.')
elif cor == "Azul":
    os.chdir('/data/data/com.termux/files/home/Color/Bash/')
    os.system('cp Azul /data/data/com.termux/files/usr/etc/')
    os.chdir('/data/data/com.termux/files/usr/etc/')
    os.system('rm -rf bash.bashrc')
    os.system('mv Azul bash.bashrc')
    print(f'\n{Vd}Pronto! \n\n')
    print('Para salvar use o comando "exit" e volte ao terminal.')
else:
    os.system("python3 color.py")
