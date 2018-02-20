from swagger_server.models.simulation import Simulation
from contextlib import redirect_stdout
import io
import os
# import subprocess
import json
import yaml

import logging

from pprint import pprint

from flask import jsonify

from cis_interface import runner

def newYamlObj(name, driver, args):
    return { 'name':name, 'driver':driver, 'args':args }
    
def getModelById(nodes, id):
    for node in nodes:
        if node.model.id == id:
            return node.model
    
def getNodeById(nodes, id):
    for node in nodes:
        if node.id == id:
            return node
    
def getModelByNodeId(nodes, id):
    for node in nodes:
        if node.id == id:
            return node.model
    
def getCountByNodeId(nodes, id):
    for node in nodes:
        if node.id == id:
            return node

# from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
# config.load_incluster_config()

#
# This file holds the server implementation called 
# into by the generated Swagger REST API
#

# Handler for GET /models
def GET_models_handler():
    basepath = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    datapath = os.path.join(basepath, 'data')
    f = open(os.path.join(datapath, 'models.json'), encoding='utf-8');
    data = json.load(f)
    return jsonify(data)

# Handler for GET /simulations
def GET_simulations_handler():
    return 'a-yup'
    
def POST_graphs_handler(body):
    # Accepts Graph model as "body"
    # Graph contains "nodes" and "edges"
    
    nodes = body.nodes
    edges = body.edges
    
    # Accumulator for our model objects
    models = []
    yaml_str = {}
    
    # Loop over each node and build a model YAML skeleton
    for node in nodes:
        # Skip inports/outports
        if node.model.name == 'inport' or node.model.name  == 'outport':
            continue
        
        # TODO: handle complex flags (e.g. is_client, is_server, etc)
        model_name = node.name
        model_driver = node.model.driver
        model_args = node.model.args
        
        model = newYamlObj(model_name, model_driver, model_args)
        
        # Initialize empty inputs/outputs
        model['inputs'] = []
        model['outputs'] = []
        
        models.append(model)
        
    for edge in edges:
        # Generate an encoded unique name for the inputs/outputs
        name = edge.source.node_id + ":" + edge.source.name + "_" + edge.destination.node_id + ":" + edge.destination.name
        
        # Lookup our src/dest models
        src = None
        dest = None
        
        logging.warning('Looking up models: ' + name)  # will print a message to the console
        for model in models:
            logging.warning('Considering ' + model['name'])
            if model['name'] == edge.source.node_id:
                logging.warning('Found src: ' + model['name'])
                src = model
            if model['name'] == edge.destination.node_id:
                logging.warning('Found dest: ' + model['name'])
                dest = model
                
        if edge.source.model_id == 'inport':
            # this is a graph inport: read from/driver/args to determine source
            # TODO: multiplex driver based on "type"
            dest['inputs'].append(newYamlObj(name + "_input", 'FileInputDriver', edge.args))
        elif edge.destination.model_id == 'outport':
            # this is a graph outport: read to/driver/args to determine destination
            # TODO: multiplex driver based on "type"
            src['outputs'].append(newYamlObj(name + "_output", 'FileOutputDriver', edge.args))
        else:
            # model-to-model connection
            # TODO: use RMQ? ZMQ?
            # NOTE: "type" and "args" need to match here
            src['outputs'].append(newYamlObj(name + "_out", 'RMQOutputDriver', name))
            dest['inputs'].append(newYamlObj(name + "_in", 'RMQInputDriver', name))
            
    yaml_str['models'] = models
            
    return yaml.dump(yaml_str, default_flow_style=False)

# DEPRECATED: Handler for POST /simulations
def POST_simulations_handler(body):
    examples_dir='/usr/local/lib/python3.6/site-packages/cis_interface/examples'
    models_dir='./Models_AMQP'

    # List of paths to yaml files specifying the models that should be run
    # TODO: Pull this from POST body instead?
    # FIXME: temporary hack
    models = body.models
    yaml_paths = []
    
    print(models)

    for model in models:
        name = model.name
        path = model.path

        # Temporary handling for running the examples
        if name.startswith('example:'):
            path = examples_dir + '/' + path + '.yml'
        else:
            path = models_dir + '/' + path + '.yml'
        yaml_paths.append(path)
        

    # Run "cisrun" with the given models and capture stdout/stderr
    f = io.StringIO()
    try: 
        with redirect_stdout(f):
            runner.get_runner(yaml_paths).run()
    except e:
        print('error: ' + e)
    return f.getvalue()
        
    # TODO: Set model parameters somehow
    # FIXME: Writing parameters to files on disk doesn't allow for 2+ users
    
    
    # Experiment: Kubernetes Python Client
    #v1 = client.CoreV1Api()
    #print("Listing pods with their IPs:")
    #ret = v1.list_pod_for_all_namespaces(watch=False)
    #for i in ret.items:
    #    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    
    # Experiment: Raw Docker
    # subprocess.check_output(['docker', 'run', '-it', '--rm', '-e', 'RABBIT_NAMESPACE=apiserver', '-e', 'RABBIT_HOST=10.0.0.214', '-e', 'YAML_FILES=' + str(yaml_paths), 'bodom0015/cis_interface'])

    #return 'did some magic!'
