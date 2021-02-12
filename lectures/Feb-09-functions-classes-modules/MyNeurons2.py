import numpy as np


brainRegion = "hippocampus"


class MySpikingNeuron:
    """ My cool neuron
    
    This neuron can spike
    and stuff!
    """
    
    def __init__(self, rate=10):
        self.spikeRatePerSec = rate
    
    def getTimeToNextSpikeInSec(self):
        return 1 / self.spikeRatePerSec
    
    def getAverageSpikeRate(self, anotherNeuron):
        return (self.spikeRatePerSec + anotherNeuron.spikeRatePerSec) / 2


def createThreeRandomNeurons():
    randomSpikeRatesPerSec = 10 / np.random.random(3)
    neurons = []
    for rate in randomSpikeRatesPerSec:
        neurons.append(MySpikingNeuron(rate))
    return neurons