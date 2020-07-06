from flask import Flask, render_template, request, flash, redirect, url_for, session
import os
import psutil
import time
import util.database_functions

app = Flask(__name__)

# Counter for ports to use when starting new nodes
port_counter = 42069
nodes = None
SCRIPT_FILE_PATH = "./util/scripts/"


def pid_stats(pid):
    process = psutil.Process(pid)
    data = dict()
    data['status'] = process.status()
    data['runtime'] = time.time() - process.create_time()
    return data


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
    data = dict()
    data["name"] = str(name)
    data["rpc_port"] = port_counter
    data["exposition_port"] = port_counter + 1
    data["conseil_port"] = port_counter + 2
    data["arronax_port"] = port_counter + 3
    data["network"] = str(request.args.get("network"))
    data["status"] = "starting"
    port_counter += 4

    # Start Node
    if request.args.get("new"):
        os.system(SCRIPT_FILE_PATH + "start_node.sh " + request.args.get("network") + " " + str(data["rpc_port"]) + " " + str(data["exposition_port"]) + " " + name)
        os.system(SCRIPT_FILE_PATH + "setup_conseil.sh " + name)
        os.system(SCRIPT_FILE_PATH + "setup_arronax.sh " + name + " " + str(data["arronax_port"]) + " " + str(data["network"]) + " " + str(data["conseil_port"]) + " " + str(data["rpc_port"]))
    else:
        os.system(SCRIPT_FILE_PATH + "restart_node.sh " + request.args.get("network") + " " + str(data["rpc_port"]) + " " + str(data["exposition_port"]) + " " + name)

    os.system(SCRIPT_FILE_PATH + "run_conseil.sh " + name + " " + str(data["rpc_port"]) + " " + str(data["network"]) + " " + str(data["conseil_port"]))

    os.system(SCRIPT_FILE_PATH + "run_arronax.sh " + name)

    # Store node process statistics
    data["status"] = "running"

    add_node(data)

    return redirect(url_for("start_page"))


@app.route("/stop_node", methods=["GET"])
def stop_node():
    os.system(SCRIPT_FILE_PATH + "stop_node.sh " + request.args.get('name'))
    os.system(SCRIPT_FILE_PATH + "stop_conseil.sh " + request.args.get('name'))
    os.system(SCRIPT_FILE_PATH + "stop_arronax.sh " + request.args.get('name'))
    update_status(request.args.get('name'), "stopped")
    return render_template("node.html", node=get_node_date(request.args.get("name")))


@app.route("/restart_node", methods=['GET'])
def restart_node():
    name = str(request.args.get("name"))
    data = get_node_date(name)
    os.system(SCRIPT_FILE_PATH + "restart_node.sh " + str(data["network"]) + " " + str(data["rpc_port"]) + " " + str(data["exposition_port"]) + " " + str(name))
    os.system(SCRIPT_FILE_PATH + "start_conseil.sh " + name + " " + str(data["rpc_port"]) + " " + str(data["network"]) + " " + str(data["conseil_port"]))
    update_status(name, "running")
    return redirect("/node?name=" + name)


@app.route("/node", methods=["GET"])
def node_page():
    return render_template("node.html", node=get_node_date(request.args.get("name")))


@app.route("/rpc", methods=['GET'])
def node_rpc_page():
    return render_template("rpc.html", node=get_node_date(request.args.get("name")))


if __name__ == "__main__":
    app.debug = True
    app.run()
    setup_database()
    global nodes
    nodes = get_all_nodes()
    global port_counter
    port_counter = get_max_port()
