from flask import Flask, render_template, request, flash, redirect, url_for, session
import os
import psutil
import time

app = Flask(__name__)

# Counter for ports to use when starting new nodes
port_counter = 42069

nodes = dict()

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
    nodes[name] = dict()
    nodes[name]["name"] = str(name)
    nodes[name]["rpc_port"] = port_counter
    nodes[name]["exposition_port"] = port_counter + 1
    nodes[name]["conseil_port"] = port_counter + 2
    nodes[name]["network"] = str(request.args.get("network"))
    nodes[name]["status"] = "starting"
    port_counter += 3

    # Start Node
    if request.arg.get("new"):
        os.system(SCRIPT_FILE_PATH + "start_node.sh " + request.args.get("network") + " " + str(nodes[name]["rpc_port"]) + " " + str(nodes[name]["exposition_port"]) + " " + name)
        os.system(SCRIPT_FILE_PATH + "setup_conseil.sh " + name)
    else:
        os.system(SCRIPT_FILE_PATH + "restart_node.sh " + request.args.get("network") + " " + str(nodes[name]["rpc_port"]) + " " + str(nodes[name]["exposition_port"]) + " " + name)

    os.system(SCRIPT_FILE_PATH + "start_conseil.sh " + name + " " + str(nodes[name]["rpc_port"]) + " " + str(nodes[name]["network"]) + " " + str(nodes[name]["conseil_port"]))

    # Store node process statistics
    nodes[name]["status"] = "running"
    nodes[name]["pid"] = os.environ["node_pid"]
    nodes[name]["process"] = psutil.Process()

    print(nodes)

    return redirect(url_for("start_page"))


@app.route("/stop_node", methods=["GET"])
def stop_node():
    os.system(SCRIPT_FILE_PATH + 'stop_node.sh ' + request.args.get('name'))
    os.system(SCRIPT_FILE_PATH + "stop_conseil.sh " + request.args.get("name"))
    nodes[request.args.get("name")]['status'] = "stopped"
    return render_template("node.html", node=nodes[request.args.get('name')])


@app.route("/restart_node", methods=['GET'])
def restart_node():
    name = str(request.args.get("name"))
    os.system(SCRIPT_FILE_PATH + "restart_node.sh " + str(nodes[name]["network"]) + " " + str(nodes[name]["rpc_port"]) + " " + str(nodes[name]["exposition_port"]) + " " + str(name))
    os.system(SCRIPT_FILE_PATH + "start_conseil.sh " + name + " " + str(nodes[name]["rpc_port"]) + " " + str(nodes[name]["network"]) + " " + str(nodes[name]["conseil_port"]))
    nodes[name]['status'] = "running"
    return redirect("/node?name=" + name)


@app.route("/node", methods=["GET"])
def node_page():
    return render_template("node.html", node=nodes[request.args.get("name")])


@app.route("/rpc", methods=['GET'])
def node_rpc_page():
    return render_template("rpc.html", node=nodes[request.args.get("name")])


if __name__ == "__main__":
    app.debug = True
    app.run()


