from nbtools import build_ui
from IPython.display import display
from urllib.request import urlopen
import builtins
import json
import re


__version__ = '1.1.0'


@build_ui(name='Cytoscape Network',
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
    # Determine if the input is a file path or URL
    is_url = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Set the opener based on local or remote
    if re.match(is_url, cx_file): open_file = urlopen
    else: open_file = builtins.open

    # Read the contents of the file
    data = ''
    with open_file(cx_file) as f:
        data = f.read()

    # Display the network
    data_json = json.loads(data)
    cx_data = {
        "application/cx": data_json
    }
    display(cx_data, raw=True)