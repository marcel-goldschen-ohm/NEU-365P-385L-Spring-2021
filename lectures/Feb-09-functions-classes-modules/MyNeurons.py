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