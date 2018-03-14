__author__ = "Alan Felix e Icaro Prado"
__date__ = "$Mar 13, 2018 20:21:00 AM$"

import sys

from experiments.episodicexperiment import EpisodicExperiment
from tasks.mariotask import MarioTask
from agents.agentealanicaro import AlanIcaro


def main():
    agent = AlanIcaro()
    task = MarioTask(agent.name, initMarioMode = 2)
    exp = EpisodicExperiment(task, agent)
    print 'Task Ready'
    exp.doEpisodes(2)
    print 'mm 2:', task.reward

    task.env.initMarioMode = 1
    task.env.levelDifficulty = 1
    exp.doEpisodes(1)
    print 'mm 1:', task.reward
    
    task.env.initMarioMode = 1
    task.env.levelDifficulty = 2
    exp.doEpisodes(1)
    print 'mm 0:', task.reward

    task.env.initMarioMode = 1
    task.env.levelDifficulty = 3
    exp.doEpisodes(1)
    print 'mm 0:', task.reward
    
    task.env.initMarioMode = 1
    task.env.levelDifficulty = 4
    exp.doEpisodes(1)
    print 'mm 0, ld 5: ', task.reward
    
    task.env.initMarioMode = 1
    task.env.levelDifficulty = 5
    exp.doEpisodes(1)
    print 'mm 1, ld 5: ', task.reward

    task.env.initMarioMode = 1
    task.env.levelDifficulty = 6
    exp.doEpisodes(1)
    print 'mm 2, ld 5: ', task.reward

    
    print "finished"

#    clo = CmdLineOptions(sys.argv)
#    task = MarioTask(MarioEnvironment(clo.getHost(), clo.getPort(), clo.getAgent().name))
#    exp = EpisodicExperiment(clo.getAgent(), task)
#    exp.doEpisodes(3)

if __name__ == "__main__":
    main()
else:
    print "This is module to be run rather than imported."
