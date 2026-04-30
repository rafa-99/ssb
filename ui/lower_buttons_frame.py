import os
import tkinter as tk
import utils.constants as C

from services.ip_utils import collect_ips, collect_all_ips
from services.firewall import generate_firewall_rules, apply_rules, remove_rules, count_rules

from tkinter import messagebox

def apply_rules_ui(tree, executable, store):
    data = store["data"]
    exe_path = executable.path.get()

    if not data:
        messagebox.showerror(C.ERROR_MESSAGE, C.ERROR_DATASET)
        return False

    selected = tree.get_selected()

    all_ips = set(collect_all_ips(data))
    allowed_ips = set(collect_ips(data, selected))

    blocked_ips = all_ips - allowed_ips

    if not blocked_ips:
        messagebox.showwarning(C.WARNING, C.WARNING_NOTHING_BLOCKED)
        return False

    rules = generate_firewall_rules(exe_path, blocked_ips, f'-{store["name"]}')
    return apply_rules(rules)

def toggle_rules(tree, executable, store, state, label_var):
    if state["value"]:
        remove_rules()
        label_var.set(C.BLOCK_SERVER)
        state["value"] = False
    else:
        if apply_rules_ui(tree, executable, store):
            label_var.set(C.UNBLOCK_SERVER)
            state["value"] = True

class LowerButtonsFrame(tk.Frame):
    def __init__(self, parent, tree, executable, data_store, rules_active):
        super().__init__(parent)

        self.tree = tree
        self.executable = executable
        self.data_store = data_store
        self.rules_active = rules_active

        self.button_text = tk.StringVar(value=C.BLOCK_SERVER)
        self.count_text = tk.StringVar(value=C.SERVER_RULES)

        tk.Button(
            self,
            textvariable=self.button_text,
            command=self.handle_toggle
        ).pack(side="left", padx=5)

        tk.Button(
            self,
            text=C.CLEANUP_RULE,
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
        if messagebox.askyesno(C.CONFIRM_MESSAGE, C.REMOVE_ALL_RULES):
            remove_rules()

            self.rules_active["value"] = False
            self.button_text.set(C.BLOCK_SERVER)

            self.update_rule_count()

    def update_rule_count(self):
        count = count_rules()
        if self.data_store["data"] is not None:
            messagebox.showinfo(C.SUCCESS_MESSAGE, f"{count} {C.FIREWALL_UPDATED}")
        self.count_text.set(f"{C.SERVER_RULES} {count}")