from turtle import Turtle

t= Turtle()
t.speed(1)

while True:
    direcao = input('Para qual direção deseja ir? (f) frente, (t) trás(s) sair: ').lower()
    if direcao == 's':
        print('Saindo do programa...')
        break
    elif direcao not in ['f', 't']:
        print('Direção inválida. Tente novamente.')
        continue
    if direcao == 'f':
        distancia = int(input('Distancia para andar: '))
        t.forward(distancia)

    elif direcao == 't':
        distancia = int(input('Distancia para andar: '))
        t.backward(distancia)
    
    rotacao = input('Para qual direção deseja rotacionar? (e) esquerda, (d) direita: ').lower()
    if rotacao not in ['e', 'd']:
        print('Rotação inválida. Tente novamente.')
        continue
    angulo = int(input('Quantos graus deseja rotacionar? '))
    if rotacao == 'e':
        t.left(angulo)  
    elif rotacao == 'd':
        t.right(angulo)
    print('Movimento concluído.')

    if input('Deseja continuar? (s/n): ').lower() != 's':
        print('Saindo do programa...')
        break
