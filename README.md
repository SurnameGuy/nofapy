# Nofapy
Programa simples escrito em Python para auxiliar os guerreiros no NOFAP, pensado especificamente para usuários de Linux.
# Exemplo
```
tux@pc:~$ nofapy
Olá! Seja bem-vindo ao Nofapy. Parece que essa é a sua primeira vez executando. Digite --help para obter uma lista de ajuda.

Tempo de NOFAP: 0 dias (0d:0h:0m:0s)
Tempo de NOPORN: 0 dias (0d:0h:0m:0s)

Motivo da última recaída: ———
tux@pc:~$ nofapy --recaida-nofap
Tem certeza que deseja resetar a sua contagem do NOFAP? (s/N): s
Digito o motivo da recaída, ou deixe em branco para pular: Me deixei vencer pela carne.
A sua contagem do NOFAP foi resetada. 
tux@pc:~$ nofapy
Tempo de NOFAP: 0 dias (0d:0h:0m:3s)
Tempo de NOPORN: 0 dias (0d:0h:0m:32s)

Motivo da última recaída: Me deixei vencer pela carne.
tux@pc:~$ nofapy --sos
Abrindo guias de emergência no seu navegador padrão...
tux@pc:~$ nofapy --recaida-geral
[...]
```
### (Dev: Para fazer)
>Consertar a discordância entre dias, meses, horas, etc., cujos valores aparecem um valor absurdamente desconexo após certas circustâncias.

# Como instalar
Para instalar, navegue até alguma pasta onde você deseja baixar o instalador, como por exemplo a sua pasta de downloads. Você pode fazer isso abrindo uma janela do terminal e digitando este comando:
```bash
cd ~/Downloads
```
Após isso, **clone esse repositório** utilizando o seguinte comando:
```bash
git clone https://github.com/SurnameGuy/nofapy
```
*(Observação: Você precisa ter o git instalado em seu computador. Caso não tenha, baixe manualmente o arquivo .zip clicando no botão ![](https://i.imgur.com/mrv5onm.png))*

Depois de ter clonado o repositório, navegue até a pasta criada:
```bash
cd nofapy
```
E então digite esse comando para executar o instalador do nofapy:
```bash
sudo python3 install.py
```
Agora siga as instruções inuitivas do instalador.

Certifique-se de que você tem o python3 instalado no seu computador antes de tentar executar o instalador, ou ele e o próprio nofapy não irão funcionar.

Para desinstalar o nofapy, é só executar o instalador novamente, e ele irá detectar a instalação, lhe fornecendo a opção para desintalar.

#FAQ
### Obter ajuda
Para obter ajuda, digite: `nofapy --help`.
### Definir manualmente o meu início do NOFAP
Essa função ainda não está disponível, porém, você pode manualmente alterar a data de início do seu NOFAP digitando:
```bash
echo -n "AAAA, MM, DD, hh, mm, ss" > ~/.config/nofapy/nofap.var
# Substitua as letras acima pelo ano, mês, dia, hora, minuto e segundo que você começou.
# Exemplo: "2020, 05, 01, 12, 30, 00" significa 01/05/2024 às 12:30:00.
```
Caso algo errado ocorra, você pode facilmente reverter ao padrão de fábrica digitando:
```bash
nofapy --reset-all```

# Como instalar o Python 3
APT (Debian/*buntu/Linux Mint/Kali Linux...):
```bash
sudo apt install python3
```
Pacman (Arch Linux/Manjaro...):
```bash
sudo pacman -Sy python-pip
```
DNF (CentOS/Fedora/RedHat/...):
```bash
sudo dnf install python3```

# Versão para Windows
Para instalar no Windows, [clique aqui](https://www.google.com/search?q=Como+desinstalar+o+Windows+e+instalar+o+Linux+no+computador).
