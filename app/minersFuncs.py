import os
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer



def alpha_model(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    log = pm4py.read_xes(filename)
    net, initial_marking, final_marking = alpha_miner.apply(log)
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    # pn_visualizer.view(gviz)  
    return pn_visualizer.view(gviz)

