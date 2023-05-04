import os
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer



def alpha_model(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    logAlpha = pm4py.read_xes(filename)
    netAlpha, initial_markingAlpha, final_markingAlpha = alpha_miner.apply(logAlpha)
    gviz = pn_visualizer.apply(netAlpha, initial_markingAlpha, final_markingAlpha)
    # pn_visualizer.view(gviz)  
    return pn_visualizer.view(gviz)

def inductive_model(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    logInduct = pm4py.read_xes(filename)
    netInduct, initial_markingInduct, final_markingInduct = alpha_miner.apply(logInduct)
    gvizInduct = pn_visualizer.apply(netInduct, initial_markingInduct, final_markingInduct)
    return pn_visualizer.view(gvizInduct)
    
