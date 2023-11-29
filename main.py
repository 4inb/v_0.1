# pip freeze requirements.txt
# install --> pip install -U g4f


import g4f.models


from g4f.gui import run_gui
import g4f

def ask_gpt(messages: list) -> str:
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=messages
        )
        print(response)
        return response
    except RuntimeError as err:
        print('Не сработало! попробую еще раз...')
        ask_gpt(messages)

messages = []

while True:
    question = str(input('Задай вопрос (или команду help):'))
    if question == 'help':
        print('''
        Команды для работы с приложением:
        \tGUI - включить веб-интерфейс,
        \tall_messages - получить все отправленные запросы,
        \texit - закрыть приложение''')
        continue
    elif question == 'GUI':
        # Запуск графического интерфейса
        run_gui()
    elif question == 'all_messages':
        print(messages)
    elif question == 'exit':
        break
    else:
        messages.append({'role': 'user', 'content': question})

    answer = ask_gpt(messages)
    messages.append({'role': 'assistant', 'content': answer})