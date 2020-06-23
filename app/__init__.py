from flask import Flask, render_template, request, flash, redirect, url_for, session
import os

app = Flask(__name__)
node_not_started = True
packages_installed = False

SCRIPT_FILE_PATH = "./util/scripts/"

@app.route("/")
def start_page():
    return render_template("index.html", node_not_started = node_not_started)

@app.route("/start_node", methods=['GET'])
def node_start_page():
    user_data = request.args
    # If statement for proper installation of dependencies
    global packages_installed
    if user_data.get("os") == "linux":
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
    if user_data.get("devmode"):
        os.system(SCRIPT_FILE_PATH + "build_tezos.sh -d")
    else:
        os.system(SCRIPT_FILE_PATH + "build_tezos.sh")
    global node_not_started
    node_not_started = False
    return redirect(url_for("start_page"))


if __name__ == "__main__":
    app.debug = True
    app.run()
