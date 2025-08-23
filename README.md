# Notificação de Estudo com Python

Este projeto envia uma notificação diária no Windows para lembrar você de estudar Automação.

## Como funciona

- Utiliza a biblioteca [`winotify`](https://github.com/kaushiknath/winotify) para criar notificações no Windows.
- A notificação é agendada para aparecer todos os dias às 08:00.
- Inclui um link para aprender Python.

## Requisitos

- Python 3.x
- Instalar dependências:
  ```sh
  pip install winotify schedule
  ```

## Como executar

1. Edite o caminho do ícone no arquivo [`app.py`](app.py) se necessário.
2. Execute o script:
   ```sh
   python app.py
   ```

## Personalização

- Altere o horário da notificação modificando:
  ```python
  schedule.every().day.at("08:00").do(tarefa)
  ```
- Modifique a mensagem, título ou link conforme desejado.

## Licença

Este projeto é apenas afins educacionais.