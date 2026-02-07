#  Weather API - Mind7 Challenge

Este é um sistema de previsão do tempo completo, desenvolvido com **Django** e **Django REST Framework**. O projeto oferece uma interface web consumindo dados em tempo real da API OpenWeather.

## Tecnologias Utilizadas

* **Backend:** Python 3.14 / Django 6.0
* **API:** Django REST Framework (DRF)
* **Autenticação:** JWT (SimpleJWT) para API e Session Auth para Web.
* **Frontend:** Tailwind CSS via CDN.
* **Dados:** Integração com OpenWeather API.
* **Banco de Dados:** SQLite.

## Funcionalidades

* **Cadastro de Usuário:** Modelo customizado com e-mail, nome, cidade e estado.
* **Clima em Tempo Real:** Visualização do clima atual com base na cidade do usuário.
* **Previsões:** Consultas para o dia seguinte e para os próximos 5 dias.
* **Conversão de Dados:** Tratamento de timestamps Unix e fuso horário (UTC-3).

## Como Rodar o Projeto

### Pré-requisitos
* Python 3.10+
* Uma chave de API da [OpenWeather](https://openweathermap.org/api)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/oandrecarvalho/weather_api.git](https://github.com/oandrecarvalho/weather_api.git)
    cd weather_api
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Mac/Linux
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto:
    ```text
    SECRET_KEY=sua_secret_key_aqui
    API_KEY=sua_chave_openweather_aqui
    ```

5.  **Rode as migrações e inicie o servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
    Acesse: `http://127.0.0.1:8000/`

---
Desenvolvido por **André Luís** como parte de um desafio técnico.