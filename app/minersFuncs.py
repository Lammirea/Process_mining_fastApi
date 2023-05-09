import os
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.utils import get_properties

def alpha_model(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    logAlpha = pm4py.read_xes(filename)
    netAlpha, initial_markingAlpha, final_markingAlpha = alpha_miner.apply(logAlpha)
    parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
    gviz = pn_visualizer.apply(netAlpha, initial_markingAlpha, final_markingAlpha,parameters=parameters,
            variant=pn_visualizer.Variants.FREQUENCY,log=logAlpha) 
    return pn_visualizer.view(gviz)

def inductive_model(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    logInduct = pm4py.read_xes(filename)
    parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
    netInduct, initial_markingInduct, final_markingInduct = pm4py.discover_petri_net_inductive(logInduct)
    gvizInduct = pn_visualizer.apply(netInduct, initial_markingInduct, final_markingInduct,parameters=parameters,
                           variant=pn_visualizer.Variants.FREQUENCY,log=logInduct)
    return pn_visualizer.view(gvizInduct)
    
def heuristics_model(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    logHeur = pm4py.read_xes(filename)
    heu_net = heuristics_miner.apply_heu(logHeur,parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.5})
    gviz = hn_visualizer.apply(heu_net)
    return hn_visualizer.view(gviz)

def conformanceChecking(filename):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    log = pm4py.read_xes(filename)
    netCheck, initial_markingCheck, final_markingCheck = pm4py.discover_petri_net_inductive(log)
    replay_result = token_replay.apply(log, netCheck, initial_markingCheck, final_markingCheck)
    gvizConform = pn_visualizer.apply(netCheck,parameters={pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"})
    return pn_visualizer.view(gvizConform)

def get_start_activities(filename):
    log = pm4py.read_xes(filename)
    from pm4py.statistics.start_activities.pandas import get
    return get.get_start_activities(log, parameters=get_properties(log))

def get_end_activities(filename):
    log = pm4py.read_xes(filename)
    from pm4py.statistics.end_activities.pandas import get
    return get.get_end_activities(log, parameters=get_properties(log))

def get_minimum_self_dist(filename):
    log = pm4py.read_xes(filename)
    from pm4py.algo.discovery.minimum_self_distance import algorithm as msd_algo
    return msd_algo.apply(log, parameters=get_properties(log))
