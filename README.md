
# Django Project - Calculadora de Raízes de Equações Quadráticas

Este projeto é uma aplicação Django que calcula as raízes de uma equação quadrática com base nos coeficientes fornecidos. Ele utiliza o modelo `CalcSqrt` para realizar os cálculos e armazenar os resultados.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- **Python 3.8+**: [Instale o Python](https://www.python.org/downloads/)
- **Django 4.0+**: Instale o Django com o comando `pip install django`
- **Virtualenv (opcional)**: Para criar um ambiente virtual isolado.

## Configuração do Projeto

Siga os passos abaixo para configurar e executar o projeto:

### 1. Clone o Repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Crie e Ative um Ambiente Virtual (opcional)

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **Linux/Mac**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instale as Dependências

Instale as dependências necessárias para o projeto:

```bash
pip install -r requirements.txt
```

> Nota: Certifique-se de que o arquivo `requirements.txt` contém Django e outras dependências necessárias.

### 4. Configure o Banco de Dados

Execute as migrações para configurar o banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Execute o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Acesse o projeto no navegador em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Uso do Modelo `CalcSqrt`

O modelo `CalcSqrt` é usado para calcular as raízes de uma equação quadrática com base nos coeficientes `a`, `b` e `c`. Siga os passos abaixo para utilizá-lo:

1. Acesse o painel de administração do Django em [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
2. Adicione uma nova entrada no modelo `CalcSqrt` fornecendo os valores para `coeficiente_a`, `coeficiente_b` e `coeficiente_c`.
3. O resultado será calculado automaticamente e salvo no campo `result_sqrt`.

## Testando o Projeto

Para testar o projeto, você pode criar entradas no banco de dados e verificar os resultados calculados. Certifique-se de que o coeficiente `a` não seja zero, pois isso resultará em um erro.

## Estrutura do Projeto

Abaixo está a estrutura básica do projeto:

```
<project_root>/
├── manage.py
├── <app_name>/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── ...
├── db.sqlite3
├── requirements.txt
└── ...
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork, crie uma branch e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.

Divirta-se explorando o Django e calculando raízes quadráticas!
