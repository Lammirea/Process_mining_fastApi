import os
import pm4py

os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

def alpha_model(filename):
    log = pm4py.read_xes(filename)
    net,initial_marking,final_marking = pm4py.discover_petri_net_alpha(log)
    return pm4py.view_petri_net(net,initial_marking,final_marking)
