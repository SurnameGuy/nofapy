#!/usr/bin/env python3

# nofapy: A free NOFAP counter program written in Python.
# Copyright (C) 2024 SurnameGuy (https://github.com/SurnameGuy)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.



import platform, os, stat, inspect, shutil
from pathlib import Path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

homepath = str(Path.home())

# Caso seja retornado um erro, essa é a variável que você deve substituir por "username = o_seu_nome_de_usuário":
username = os.getenv('SUDO_USER')
# ---------------------------------------------------------------------------------------------------------------

try:
    if (len(username) < 1) or (username.lower() == "root"):
        print(f'''ERRO CRÍTICO. O instalador foi encerrado inesperadamente para evitar possíveis problemas. Se você acha que isso é um engano, edite o script do instalador e substitua "username = os.getenv('SUDO_USER')" por "username = " e o seu nome de usuário. FAÇA ISSO POR SUA CONTA E RISCO!!!

    Código do erro: INVALID_USERNAME_VARIABLE | Variable username = {username}''')
        exit()
except:
    None

def deletefile(filepath):
    try:
        return os.remove(filepath)
    except:
        return None

def install():
    if os.path.isfile("/usr/bin/nofapy") == True:
        confirm = input("O Nofapy já está instalado no seu sistema. Deseja desinstalá-lo? (s/N): ")
        if confirm.lower() == "s":
            confirm = input("Deseja também remover os arquivos do Nofapy (i.e, seus dados)? (s/N): ")
            if confirm.lower() == "s":
                shutil.rmtree(f"/home/{username}/.config/nofapy")
                print(f'· Deletado "/home/{username}/.config/nofapy" (shutil.rmtree ...)')
                deletefile("/usr/bin/nofapy")
                print(f'· Deletado "/usr/bin/nofapy" (os.remove ...)')
                print(f'· Nofapy desinstalado sem manter os dados do usuário.')
                exit()
            else:
                deletefile(f"/usr/bin/nofapy")
                print(f'· Deletado "/usr/bin/nofapy" (os.remove ...)')
                print(f'· Nofapy desinstalado mantendo os dados do usuário.')
        else:
            print("Cancelado.")
            exit()
    else:
        confirm = input("Deseja instalar o Nofapy no seu sistema? (s/N): ")
        if confirm.lower() == "s":
            nofapypath = f"{path}/nofapy"
            shutil.copyfile(nofapypath, "/usr/bin/nofapy")
            print(f'· Copiado "{nofapypath}" para "/usr/bin/nofapy" (shutil.copyfile ...)')
            os.chmod("/usr/bin/nofapy", 0o777)
            print(f'· Definido "/usr/bin/nofapy" como executável (os.chmod 777)')
            print(f'· Instalado! Para executar, apenas digite "nofapy" no seu terminal. Caso não funcionar, tente fechar e abrir novamente o seu terminal antes de executá-lo pela primeira vez.')
        else:
            print("Cancelado.")
            exit()
    
if platform.system() == "Linux":
    if not 'SUDO_UID' in os.environ:
        print("ERRO: Este programa requer ser executado com privilégios de super-usuário!")
        exit()
    install()
else:
    confirm = input("Parece que você não está utilizando Linux. Este software não foi testado em outras plataformas, e não me responsabilizo por qualquer problema envolvendo seu funcionamento. Deseja continuar mesmo assim? (s/N): ")
    if confirm.lower() == "s":
        install()
    else:
        exit()
