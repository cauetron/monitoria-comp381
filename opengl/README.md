# Como instalar o PyOpenGL e o freeglut3-dev numa distribuição Ubuntu

Primeiro instale o `pip3`

```shell
sudo apt update
sudo apt install python3-pip
```

Verifique qual versão de Python é executada em  `python3`

```shell
python3 --version
```

Em Python é sempre uma boa ideia trabalhar em um ambiente virtual. Para isso, você precisa instalar um ambiente virtual `venv` compatível com a versão de Python que você vai utilizar. No meu caso,  `Python 3.10.4`

```shell
sudo apt install python3.10-venv
```

Clone este repositório e abra o terminal no diretório `monitoria-comp381`

Depois disso, crie e ative o ambiente virtual no diretório `opengl/venv`

```bash
python3 -m venv opengl/venv
source opengl/venv/bin/activate
```

Você deve notar uma alteração no seu *bash prompt*, com o nome do ambiente virtual entre parenteses antes do seu *username*: `(venv) username@hostname:`

Recomendo que você só prossiga com a instalação do PyOpenGL após ter conseguido concluir as etapas anteriores.

Por fim, instale o PyOpenGL e o freeglut3-dev

```shell
pip3 install PyOpenGL
sudo apt install freeglut3-dev
```

Para testar se a instação foi bem sucedida, execute o seguinte arquivo

```shell
python3 opengl/src/01_Hello_World/hello_world.py
```

Você deve visualizar uma janela chamada Hello World 640x640 com fundo preto contendo um triângulo colorido.

![Captura de tela de uma janela chamada Hello World 640x640 com fundo preto contendo um triângulo colorido](https://user-images.githubusercontent.com/34218434/189769596-512b8ec9-fb41-4e7c-9179-0760436b4c8b.png)
