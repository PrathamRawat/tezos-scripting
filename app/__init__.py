from flask import Flask, render_template, request, flash, redirect, url_for, session
import os

app = Flask(__name__)
node_not_started = True
node_setup = False
packages_installed = False
code_installed = False

SCRIPT_FILE_PATH = "./util/scripts/"

@app.route("/")
def start_page():
    return render_template("index.html", node_not_started = node_not_started)


@app.route("/loading/<redirect_function>")
def loading_page(redirect_function):
    return redirect(url_for(redirect_function))


@app.route("/start_node", methods=['GET'])
def node_start_page():
    # If the node has not been setup before
    global node_setup
    if not node_setup:
        # If statement for proper installation of dependencies
        global packages_installed
        if request.args.get("os") == "linux":
            # Install packages for linux if not installed
            if not packages_installed:
                os.system(SCRIPT_FILE_PATH + "install_packages.sh -l")
                packages_installed = True
        else:
            # Install packages for macOS using homebrew if not installed
            if not packages_installed:
                os.system(SCRIPT_FILE_PATH + "install_packages.sh -m")
                packages_installed = True
        os.system(SCRIPT_FILE_PATH + "setup_tezos.sh")
        # Build with developer dependencies or not
        if request.args.get("devmode"):
            os.system(SCRIPT_FILE_PATH + "build_tezos.sh -d")
        else:
            os.system(SCRIPT_FILE_PATH + "build_tezos.sh")
        node_setup = True
    os.system(SCRIPT_FILE_PATH + "start_node.sh " + request.args.get("network"))
    global node_not_started
    node_not_started = False
    return redirect(url_for("start_page"))


@app.route("/rpc")
def node_rpc_page():
    return render_template("rpc.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
