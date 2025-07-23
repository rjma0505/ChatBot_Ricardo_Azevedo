import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #    return 'Olá tudo bem!'
    #if comando == 'como estás':
    #    return 'Estou bem, obrigado!'
    #if comando == 'como te chamas?':
    #    return 'O meu nome é: Bot :)'
    #if comando == 'tempo':
    #    return 'Está um dia de sol!'
    #if comando in ('bye', 'adeus', 'tchau'):
    #    return 'Gostei de falar contigo! Até breve...'
    #if 'horas' in comando:
    #    return f'São: {datetime.now():%H:%M} horas'
    #if 'data' in comando:
    #    return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    #return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
         ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
         'como estás': 'Estou bem, obrigado!',
         ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
         'como te chamas?': 'O meu nome é Bot :)',
        'tempo': 'Está um dia de sol!',
        'horas': f'São: {datetime.now():%H:%M} horas',
        'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        'qual é o teu criador?': 'Fui criado por um programador em Python.',
        'o que fazes?': 'Eu sou um chatbot e posso conversar contigo sobre diversos assuntos!',
        'ajuda': 'Posso responder a perguntas sobre o tempo, a data, as horas, e muito mais!',
        'qual a tua cor favorita?': 'Não tenho cor favorita, sou um programa de computador!',
        'tens sentimentos?': 'Como inteligência artificial, não tenho sentimentos, mas estou aqui para te ajudar!',
        'onde vives?': 'Eu vivo no ciberespaço!',
        'qual o teu objetivo?': 'O meu objetivo é auxiliar nas tuas perguntas e tornar a tua experiência mais fácil.',
        'conta-me uma piada': 'O que o tomate foi fazer no banco? Foi tirar um extrato!',
        'estás aborrecido?': 'Nunca me aborreço, estou sempre pronto para aprender e interagir!',
        'o que é python?': 'Python é uma linguagem de programação muito popular e poderosa.',
        'obrigado': 'De nada! Fico feliz em ajudar.',
     }

    for chave, resposta in respostas.items():
         if isinstance(chave, tuple):
             if comando in chave:
                 return resposta
         elif chave in comando:
             return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)
        print(f'Bot:{resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()