class Robo:
    def __init__(self, pos_x, pos_y, pos_cam):
        self.pos_x = '0'
        self.pos_y = '0'
        self.pos_cam = 'n'

    #MÉTODO QUE MOSTRA O TAMANHO DO TERRENO DE 5X5
    def terreno(self):
        if pos_x < 0 or pos_x > 5 or pos_y < 0 or pos_y > 5:
            return "O robô não pode andar nesta área, pois não faz parte do terreno!"  
        else:
            return posicao_atual

    def andar(self, m):
        pass

    #MÉTODO DE ROTACIONAR O ROBO PARA 'L' (LEFT) E 'R' (RIGHT)
    def rotacionar(self, l, r):
        self.pos_cam = 'n'
        #ROTAÇÃO COM L
        if (rotacao == 'l' & pos_cam == 'n'):
            return pos_cam == 'w'
        elif(rotacao == 'l' & pos_cam == 'w'):
            return pos_cam == 's'
        elif(rotacao == 'l' & pos_cam == 's'):
            return pos_cam == 'e'
        elif(rotacao == 'l' & pos_cam == 'e'):
            return pos_cam == 'n'
        #ROTAÇÃO COM R
        elif (rotacao == 'r' & pos_cam == 'n'):
            return pos_cam == 'e'
        elif(rotacao == 'r' & pos_cam == 'e'):
            return pos_cam == 's'
        elif(rotacao == 'l' & pos_cam == 's'):
            return pos_cam == 'w'
        else:
            return pos_cam == 'n'

    #MÉTODO QUE MOSTRA A POSIÇÃO DO ROBO APÓS O USUÁRIO PASSAR AS COORDENADAS        
    def posicao_atual(self):
        pass


    teste = Robo()
    teste1 = Robo