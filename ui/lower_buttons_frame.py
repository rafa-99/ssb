import os
import tkinter as tk

from services.ip_utils import collect_ips
from services.firewall import generate_firewall_rules, apply_rules, remove_rules, count_rules

blockServerString = "Block Servers"
unblockServerString = "Unblock Servers"
cleanupRulesString = "Cleanup all Server Rules"
datasetErrorString = "No dataset loaded"
ipErrorString = "No IPs found"
activeRulesString = "Server Rules:"

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

        self.tree = tree
        self.executable = executable
        self.data_store = data_store
        self.rules_active = rules_active

        self.button_text = tk.StringVar(value=blockServerString)
        self.count_text = tk.StringVar(value=activeRulesString)

        tk.Button(
            self,
            textvariable=self.button_text,
            command=self.handle_toggle
        ).pack(side="left", padx=5)

        tk.Button(
            self,
            text=cleanupRulesString,
            command=self.handle_cleanup
        ).pack(side="left", padx=5)

        tk.Label(
            self,
            textvariable=self.count_text
        ).pack(side="right", padx=5)

        self.update_rule_count()

    def handle_toggle(self):
        toggle_rules(
            self.tree,
            self.executable,
            self.data_store,
            self.rules_active,
            self.button_text
        )

        self.update_rule_count()

    def handle_cleanup(self):
        remove_rules()

        self.rules_active["value"] = False
        self.button_text.set(blockServerString)

        self.update_rule_count()

    def update_rule_count(self):
        count = count_rules()
        self.count_text.set(f"{activeRulesString} {count}")