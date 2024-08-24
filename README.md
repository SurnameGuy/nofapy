# Nofapy (v2.0)
Um programa CLI simples e sem dependências escrito em Python para auxiliar os guerreiros no NOFAP, pensado especificamente para usuários de Linux.
# Exemplo
```
tux@nix:~$ nofapy
Olá! Seja bem-vindo ao Nofapy. Parece que essa é a sua primeira vez executando o programa. Digite --help para obter uma lista de ajuda.
Tempo de NOFAP: 0 dia (0h:00m:00s)
Tempo de NOPORN: 0 dia (0h:00m:00s)

Motivo da última recaída: ———
tux@nix:~$ nofapy --recaida-nofap
Tem certeza que deseja resetar a sua contagem do NOFAP? (s/N): s
Digito o motivo da recaída, ou deixe em branco para pular: Eu falhei miseravelmente com Deus e comigo mesmo.
A sua contagem do NOFAP foi resetada. Execute o Nofapy quando estiver pronto para re-começar a sua contagem do NOFAP.
tux@nix:~$ nofapy
Tempo de NOFAP: 0 dia (0h:00m:00s)
Tempo de NOPORN: 0 dia (0h:00m:50s)

Motivo da última recaída: Eu falhei miseravelmente com Deus e comigo mesmo.
tux@nix:~$ nofapy --emergencia
Abrindo guias de emergência no seu navegador padrão...
[...]
```
### TO DO: O que ainda deve ser feito
>✅ [FEITO] Consertar a discordância entre dias, meses, horas, etc., cujos valores aparecem um valor absurdamente desconexo após certas circustâncias.

>🕒️ [PENDENTE] Adicionar opção para definir manualmente a data de início do NOFAP ou do NOPORN.

>🕒️ [PENDENTE] Criar uma GUI (Interface gráfica), e tornar o CLI (Interface de linha de comandos) opcional.

# Como instalar
Para instalar, navegue até alguma pasta onde você deseja baixar o instalador, como por exemplo a sua pasta de downloads. Você pode fazer isso abrindo uma janela do terminal e digitando este comando:
```bash
cd ~/Downloads
```
Após isso, **clone esse repositório** utilizando o seguinte comando:
```bash
git clone https://github.com/SurnameGuy/nofapy
```
*(Observação: Você precisa ter o git instalado em seu computador para clonar o repositório pelo terminal. Caso não tenha, baixe manualmente o arquivo .zip clicando no botão ![](https://i.imgur.com/mrv5onm.png))*

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
Essa função ainda não está disponível, porém, você pode manualmente alterar a data de início do seu NOFAP e NOPORN. Primeiro, digite:
```bash
nofapy --recaida-geral```
E depois altere o horário do seu computador para a data de quando você começou a sua jornada de castidade. Finalmente, execute:
```bash
nofapy```
Então a data será corrigida. Mas caso algo errado ocorra, você pode facilmente reverter ao padrão de fábrica digitando:
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
