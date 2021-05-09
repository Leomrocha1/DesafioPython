class Robo:
    def __init__(self, pos_inicial_x, pos_inicial_y, pos_inicial_cam):
        '''Instância a classe com seus devidos parâmetros.'''
        self.__pos_x = pos_inicial_x
        self.__pos_y = pos_inicial_y
        self.__pos_cam = pos_inicial_cam

    def get_pos_x(self):
        '''Retorna a posição x do robô.'''
        return self.__pos_x

    def set_pos_x(self, nova_pos_x):
        '''Altera o valor da posição x.''' 
        self.__pos_x = nova_pos_x

    def get_pos_y(self):
        '''Retorna a posição y do robô.'''
        return self.__pos_y

    def set_pos_y(self, nova_pos_y):
        '''Altera o valor da posição y.''' 
        self.__pos_y = nova_pos_y

    def get_pos_cam(self):
        '''Retorna a posição da câmera do robô.'''
        return self.__pos_cam

    def set_pos_cam(self, nova_pos_cam):
        '''Altera o valor da posição da câmera.''' 
        self.__pos_cam = nova_pos_cam 

    def get_posicao_atual(self):
        '''Retorna todas as posições do robô'''
        print('POSICAO ATUAL: x: {}, y: {}, camera: {}'.format
             (self.get_pos_x(), self.get_pos_y(), self.get_pos_cam())) 

    def andar(self, tamanho_max):
        '''Faz com que o robô ande para frente, mas depende da posição da \
câmera para indicar a direção que ele vai.'''
        if (self.__pos_cam == 'n' and self.__pos_y < tamanho_max):
            self.__pos_y += 1
        elif (self.__pos_cam == 'e' and self.__pos_x < tamanho_max):
            self.__pos_x += 1
        elif (self.__pos_cam == 's' and self.__pos_y > 0):
            self.__pos_y -= 1
        elif(self.__pos_cam == 'w' and self.__pos_x > 0):
            self.__pos_x -= 1
        else:
            print('O robo nao pode acessar essa area!')
            return 1
        self.get_posicao_atual()
        return 0

    def rotacionar(self, rotacao):
        '''Faz com que o robô rotacione para l (left) ou r (right), para que \
ele fique virado para o lado desejado.'''
        if (rotacao == 'l' and self.__pos_cam == 'n'):
            self.__pos_cam = 'w'
        elif(rotacao == 'l' and self.__pos_cam == 'w'):
            self.__pos_cam = 's'
        elif(rotacao == 'l' and self.__pos_cam == 's'):
            self.__pos_cam = 'e'
        elif(rotacao == 'l' and self.__pos_cam == 'e'):
            self.__pos_cam = 'n'
        elif (rotacao == 'r' and self.__pos_cam == 'n'):
            self.__pos_cam = 'e'
        elif(rotacao == 'r' and self.__pos_cam == 'e'):
            self.__pos_cam = 's'
        elif(rotacao == 'r' and self.__pos_cam == 's'):
            self.__pos_cam = 'w'
        elif(rotacao == 'r' and self.__pos_cam == 'w'):
            self.__pos_cam = 'n'
        else:
            print ('Digite apenas os comandos "l" para left e "r" para right.')
            return 1
        self.get_posicao_atual()
        return 0


class Terreno:
    def __init__(self, tamanho):
        '''Instância a classe com seus devidos parâmetros.'''
        self.__tamanho = tamanho

    def get_tamanho(self):
        '''Retorna o tamanho do terreno.'''
        return self.__tamanho

    def set_tamanho(self, novo_tamanho):
        '''Altera o valor do terreno.''' 
        self.__tamanho = novo_tamanho


class Marte:
    def __init__(self):
        '''Instância as casses Robo com posição inicial de (0,0,'n') e Terreno\
com tamanho 5'''
        self.robo = Robo(0, 0, 'n')
        self.terreno = Terreno(5)

    def explorar(self, comando):
        '''Verifica o comando que o usuário passar e o executa.'''
        if (comando == 'm'):
            return self.robo.andar(self.terreno.get_tamanho())
        elif(comando == 'l' or comando == 'r'):
            return self.robo.rotacionar(comando)
        else:
            print('Digite apenas "m" para mover, "l" para rotacionar para \
left, "r" para rotacionar right e "s" para sair.')
            return 1

def main():
    '''Função principal do sistema'''
    print('Bem-vindo a Marte! Posição inicial do Robô (0,0,"n")')

    # Instânciando a classe Marte
    marte = Marte()

    while True:
        comando = input("Informe o comando que deseja efetuar m(mover), \
l(rotacionar left), r(rotacionar right) e s(sair): ")

        if(comando == 's'):
            break
        marte.explorar(comando)

# Chamando a função principal
if __name__ == '__main__':
    main()




