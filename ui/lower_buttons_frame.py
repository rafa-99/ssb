import os
import tkinter as tk

from services.ip_utils import collect_ips
from services.firewall import generate_firewall_rules, apply_rules, remove_rules

blockServerString = "Block Servers"
unblockServerString = "Unblock Servers"
cleanupRulesString = "Cleanup Rules"
datasetErrorString = "No dataset loaded"
ipErrorString = "No IPs found"

def apply_rules_ui(tree, executable, store):
    data = store["data"]
    exe_path = executable.path.get()

    if not data:
        print(datasetErrorString)
        return

    selected = tree.get_selected()
    ips = collect_ips(data, selected)

    if not ips:
        print(ipErrorString)
        return

    rules = generate_firewall_rules(exe_path, ips, f'-{store["name"]}')

    apply_rules(rules)

def toggle_rules(tree, executable, store, state, label_var):
    if state["value"]:
        remove_rules()
        label_var.set(blockServerString)
        state["value"] = False
    else:
        apply_rules_ui(tree, executable, store)
        label_var.set(unblockServerString)
        state["value"] = True

class LowerButtonsFrame(tk.Frame):
    def __init__(self, parent, tree, executable, data_store, rules_active):
        super().__init__(parent)

        self.button_text = tk.StringVar(value=blockServerString)

        tk.Button(
            master=self,
            textvariable=self.button_text,
            command=lambda: toggle_rules(tree, executable, data_store, rules_active, self.button_text)
        ).pack(side="left", padx=5)

        tk.Button(
            master=self,
            text=cleanupRulesString,
            command=remove_rules
        ).pack(side="left", padx=5)