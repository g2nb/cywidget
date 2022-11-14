from nbtools import build_ui
from IPython.display import display
import json


__version__ = '1.0.0'


@build_ui(name='Display Cytoscape Network',
          description='Displays a Cytoscape network in the notebook.',
          origin='+',
          color='rgb(210, 140, 34)',
          parameters={
              'cx_file': {
                  'required': True,
                  'description': 'Select a Cytoscape network to view',
                  'type': 'file',
                  'kinds': ['cx']
              }
          })
def display_cytoscape_network(cx_file=''):
    data = ''
    with open(cx_file) as f:
        data = f.read()

    data_json = json.loads(data)
    cx_data = {
        "application/cx": data_json
    }

    display(cx_data, raw=True)