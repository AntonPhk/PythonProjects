# This is a small project, witch realise 'Magic Ball' functions.
# Start the code and follow instructions for touching something incredible



from random import choice

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


def magic_ball_eight():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    user_name = input('Как тебя зовут?\n')
    print(f'Привет {user_name}')
    while True:
        print('Что ты хочешь узнать у меня?')
        user_question = input()
        answer_the_question = choice(answers)
        print(answer_the_question)
        continue_choice = input('Хочешь задать еще один вопрос?\n')
        if continue_choice.lower() == 'да' or continue_choice.lower() == 'yes':
            continue
        else:
            print('Возврашайся, если возникнут вопросы.')
            break





magic_ball_eight()