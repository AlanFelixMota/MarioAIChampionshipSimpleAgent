__author__ = "Alan Felix e Icaro Prado"
__date__ = "$Mar 13, 2018 20:21:00 AM$"

import numpy

from marioagent import MarioAgent

class AlanIcaro(MarioAgent):
    action = None
    actionStr = None
    KEY_LEFT = 2
    KEY_RIGHT = 1
    KEY_JUMP = 3
    KEY_SPEED = 4
    levelScene = None
    mayMarioJump = None
    isMarioOnGround = None
    marioFloats = None
    enemiesFloats = None
    isEpisodeOver = False

    trueJumpCounter = 0;
    trueSpeedCounter = 0;


    def reset(self):
        self.isEpisodeOver = False
        self.trueJumpCounter = 0;
        self.trueSpeedCounter = 0;
        
    def __init__(self):
        """Construtor"""
        self.trueJumpCounter = 0
        self.trueSpeedCounter = 0
        self.action = numpy.zeros(5, int)
        self.action[1] = 1
        self.actionStr = ""

# dangerOfGap e uma funcao para verificar se ha buracos nas proximidades do Mario.        
    def _dangerOfGap(self):
        for x in range(9, 13):
            f = True
            for y in range(12, 22):
                if  (self.levelScene[y, x] != 0):
                    f = False
            if (f and self.levelScene[12, 11] != 0):
                return True
        return False


# A funcao getAction e responsavel pelas acoes do agente. E onde geralmente e colocada a logica dos algoritmos. E possivel utilizar as observacoes do mundo para auxiliar na decisao de quais acoes tomar, dependendo da sua abordagem. No nosso caso, o agente faz observacoes simples com relacao ao array que representa os objetos que estao na tela na hora da execucao.

    def getAction(self):
        danger = self._dangerOfGap()
	# Verificamos se ha obstaculos ou buracos em frente ao Mario. Checamos 3 posicoes a frente.
        if (self.levelScene[11, 12] != 0 or \
            self.levelScene[11, 13] != 0 or \
            self.levelScene[11, 14] != 0 or danger):

            if (self.mayMarioJump or \
                (not self.isMarioOnGround and self.action[self.KEY_JUMP] == 1)):
                self.action[self.KEY_JUMP] = 1
            self.trueJumpCounter += 1
        else:
            self.action[self.KEY_JUMP] = 0;
            self.trueJumpCounter = 0

# Aqui testamos se existem blocos acima da cabeca do Mario, checando dois niveis acima para blocos mais altos. Tambem checamos se o caminho a frente do Mario esta vazio, para que ele nao pule em um bloco e se machuque em seguida
        if (self.levelScene[12, 11] or self.levelScene[13, 11] == 21):
            if (self.levelScene[11, 12] == 0 or \
                self.levelScene[11, 13] == 0):
                if (self.mayMarioJump or \
                    (not self.isMarioOnGround and self.action[self.KEY_JUMP] == 1)):
                    self.action[self.KEY_JUMP] = 1
                self.trueJumpCounter += 1
        
        if (self.trueJumpCounter > 16):
            self.trueJumpCounter = 0
            self.action[self.KEY_JUMP] = 0;

        return self.action

# Este metodo armazena a observacao dentro do agente
    def integrateObservation(self, obs):
        if (len(obs) != 6):
            self.isEpisodeOver = True
        else:
            self.mayMarioJump, self.isMarioOnGround, self.marioFloats, self.enemiesFloats, self.levelScene, dummy = obs
#        self.printLevelScene()

# Imprime na tela o nivel em tempo real
    def printLevelScene(self):
        ret = ""
        for x in range(22):
            tmpData = ""
            for y in range(22):
                tmpData += self.mapElToStr(self.levelScene[x][y]);
            ret += "\n%s" % tmpData;
        print ret

# Mapeia os elementos do nivel para uma representacao em string, para que possa ser chamado pelo metodo printLevelScene
    def mapElToStr(self, el):
        s = "";
        if  (el == 0):
            s = "##"
        s += "#MM#" if (el == 95) else str(el)
        while (len(s) < 4):
            s += "#";
        return s + " "

    def printObs(self):
        """for debug"""
        print repr(self.observation)
