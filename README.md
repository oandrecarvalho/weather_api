# Desafio Técnico: Backend Developer - Weather API

Este projeto consiste em uma API REST desenvolvida para um sistema de gestão de usuários que permite o monitoramento da previsão do tempo baseada em suas localidades. 

O projeto utiliza **Python** com o framework **Django** e **Django Rest Framework (DRF)**.

---
##  Tecnologias Utilizadas
- **Python 3** 
- **Django** 
- **Django Rest Framework (DRF)** 
- **Simple JWT** (Para autenticação futura) 
- **SQLite** (Banco de dados inicial) 
---
##  Pré-requisitos
Antes de começar, você precisará ter o Python 3 instalado em sua máquina.

---
##  Instalação e Execução

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/oandrecarvalho/weather_api
   cd weather_api
2. **Criar e ativar o ambiente virtual:** 
    ```bash 
    (venv) python3 -m venv venv
    source venv/bin/activate  # No macOS/Linux
3. **Instalar as dependências:** 
    ```bash
    pip install -r requirements.txt

4. **Executar as migrações iniciais:** 
    ```bash
    python manage.py migrate

5. **Rodar o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    O servidor estará disponível em http://127.0.0.1:8000/. 
---

