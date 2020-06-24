from flask import Flask, render_template, request, flash, redirect, url_for, session
import os

app = Flask(__name__)

# Environment variables
node_setup = False
packages_installed = False

# Counter for ports to use when starting new nodes
port_counter = 42069

nodes = dict()

SCRIPT_FILE_PATH = "./util/scripts/"


@app.route("/")
def start_page():
    return render_template("index.html", nodes=nodes)


@app.route("/node_setup")
def new_node_setup():
    return render_template("node_options.html")


@app.route("/start_node", methods=['GET'])
def node_start_page():

    # Store the name of this new node
    name = request.args.get("name")
    if name in nodes:
        flash("The name you have provided is already being used.", "error")
        return render_template("node_options.html")

    # Store data for this network
    global port_counter
    nodes[name] = dict()
    nodes[name]["name"] = name
    nodes[name]["rpc_port"] = port_counter
    nodes[name]["exposition_port"] = port_counter + 1
    nodes[name]["network"] = request.args.get("network")
    nodes[name]["status"] = "starting"
    port_counter += 2

    # If nodes have not been setup before, setup the code base
    global node_setup
    if not node_setup:
        global packages_installed
        if not packages_installed:
            os.system(SCRIPT_FILE_PATH + "install_packages.sh")
            packages_installed = True
            os.environ['packages_installed'] = str(True)
        os.system(SCRIPT_FILE_PATH + "setup_tezos.sh")
        # Build with developer dependencies or not
        if request.args.get("devmode"):
            os.system(SCRIPT_FILE_PATH + "build_tezos.sh -d")
        else:
            os.system(SCRIPT_FILE_PATH + "build_tezos.sh")
        node_setup = True
        os.environ['node_setup'] = str(True)

    # Start Node
    os.system(SCRIPT_FILE_PATH + "start_node.sh " + request.args.get("network"))
    nodes[name]["status"] = "running"

    return redirect(url_for("start_page"))


@app.route("/node", methods=["GET"])
def node_page():
    return render_template("node.html", node_data=nodes[request.args.get("name")])


@app.route("/rpc", methods=['GET'])
def node_rpc_page():

    return render_template("rpc.html")


if __name__ == "__main__":

    # Set code variables with environment variables
    if 'node_setup' in os.environ:
        node_setup = bool(os.environ['node_setup'])
    else:
        os.environ['node_setup'] = str(node_setup)
    if 'packages_installed' in os.environ:
        packages_installed = bool(os.environ['packages_installed'])
    else:
        os.environ['packages_installed'] = str(packages_installed)

    app.debug = True
    app.run()


