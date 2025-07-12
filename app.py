from time import sleep
from winotify import Notification, audio
import schedule


def tarefa():
    notificacao = Notification(app_id="Python", title="Hora de estudar", 
                        msg="Vamos estudar Automação", 
                        duration="long", icon="C://Users/cleve/Downloads/Imagens/Python.jpeg")
    notificacao.set_audio(audio.LoopingCall10, loop=True)
    notificacao.add_actions(label="Aprender Python", launch="https://membros.devaprender.com")

    notificacao.show()

schedule.every().day.at("08:00").do(tarefa)
while True:
    schedule.run_pending()
    sleep(1)
      
