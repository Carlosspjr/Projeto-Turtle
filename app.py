from turtle import Turtle

t= Turtle()
t.speed(1)

def obter_distancia():
        resposta=int(input('Distancia para andar: '))
        return resposta

def rotacionar_turtle(turtle):
    rotacao = input('Para qual direção deseja rotacionar? (e) esquerda, (d) direita: ').lower()
    if rotacao == 'e':
        rotacionar_esquerda(turtle)
    elif rotacao == 'd':
        rotacionar_direita(turtle)
    print('Movimento concluído.')

def rotacionar_direita(turtle):
    angulo = int(input('Quantos graus deseja rotacionar? '))
    t.right(angulo)

def rotacionar_esquerda(turtle):
    angulo = int(input('Quantos graus deseja rotacionar? '))
    t.left(angulo)

while True:
    direcao = input('Para qual direção deseja ir? (f) frente, (t) trás(s) sair: ').lower()
    if direcao == 's':
        print('Saindo do programa...')
        break
    elif direcao not in ['f', 't']:
        print('Direção inválida. Tente novamente.')
        continue
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)

    elif direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
        
    if input('Deseja continuar? (s/n): ').lower() != 's':
        print('Saindo do programa...')
        break
