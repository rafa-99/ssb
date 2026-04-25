import tkinter as tk
from model.tree_model import set_children, get_selected_paths

TREE_HEIGHT = 300

class TreeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.model = []

        self.canvas = tk.Canvas(self, height=TREE_HEIGHT)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width)
        )
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def load_data(self, data):
        from model.tree_model import build_model
        self.model = build_model(data)
        self.render()

    def render(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for node in self.model:
            self.render_node(self.scrollable_frame, node, 0)

    def render_node(self, parent, node, level):
        frame = tk.Frame(parent)
        frame.pack(anchor="w", padx=level * 20)

        def toggle_expand():
            node.expanded = not node.expanded
            self.render()

        def toggle_check():
            new_state = not node.checked
            node.checked = new_state
            set_children(node, new_state)
            self.render()

        btn = tk.Button(
            frame,
            text="-" if node.expanded else "+",
            width=2,
            command=toggle_expand
        )
        btn.pack(side="left")

        cb = tk.Checkbutton(frame, text=node.name, command=toggle_check)

        if node.checked:
            cb.select()
        else:
            cb.deselect()

        cb.pack(side="left")

        if node.expanded:
            for child in node.children:
                self.render_node(parent, child, level + 1)

    def get_selected(self):
        results = []
        for node in self.model:
            results.extend(get_selected_paths(node))
        return results