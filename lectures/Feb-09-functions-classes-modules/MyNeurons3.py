import numpy as np
import MyNeurons


brainRegion = "hippocampus"


def createThreeRandomNeurons():
    randomSpikeRatesPerSec = 10 / np.random.random(3)
    neurons = []
    for rate in randomSpikeRatesPerSec:
        neurons.append(MyNeurons.MySpikingNeuron(rate))
    return neurons