# cywidget
cywidget is user-friend widget for [JupyterLab](http://jupyter.org/) that accepts a Cytoscape file and visualizes the network

igv-jupyter is tool for [JupyterLab](http://jupyter.org/) which wraps [igv.js](https://github.com/igvteam/igv.js) and
integrates with [g2nb](https://github.com/g2nb/g2nb). With this tool you can render igv.js in a cell and call its API
from a user-friendly web form in the notebook. Track data can be loaded from local or remote URLs, or supplied directly.

For programmatic access to Cytoscape in a Jupyter notebook, see [cy-jupyterlab](https://github.com/idekerlab/cy-jupyterlab).

## Installation

Requirements:

* python >= 3.7
* jupyterlab >= 3.0
* cy-jupyterlab

```bash
pip install cywidget
```