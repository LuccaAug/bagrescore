# Guia de Instalação e Execução

Este guia descreve os passos para instalar o Python 3.12 e os pacotes Flask, Flask-Login e Flask-SQLAlchemy, bem como rodar um site baseado no arquivo `main.py`.

## Requisitos

- Sistema operacional Windows, macOS ou Linux
- Acesso ao terminal ou prompt de comando

## Passo 1: Instalar o Python 3.12

1. Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe a versão 3.12 compatível com seu sistema operacional.
3. Durante a instalação, marque a opção **"Add Python to PATH"**.
4. Conclua a instalação e verifique se está correto executando o seguinte comando no terminal:
   ```sh
   python --version
   ```
   ou
   ```sh
   python3 --version
   ```
   Certifique-se de que a versão exibida seja **Python 3.12**.

## Passo 2: Criar e ativar um ambiente virtual

Para manter as dependências organizadas, recomenda-se criar um ambiente virtual:

```sh
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

## Passo 3: Instalar dependências

Com o ambiente virtual ativado, instale os pacotes necessários:

```sh
pip install flask flask-login flask-sqlalchemy
```

## Passo 4: Executar o site

Se o arquivo `main.py` contiver a definição do aplicativo Flask, execute o seguinte comando para iniciar o servidor:

```sh
python main.py
```

Caso esteja usando Linux ou macOS e a instalação seja para `python3`, rode:

```sh
python3 main.py
```

O servidor Flask será iniciado em `http://127.0.0.1:5000/`.

Agora você pode acessar o site pelo navegador e começar a desenvolver sua aplicação!

