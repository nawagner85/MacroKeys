import yaml
from tkinter import Tk, Label, Entry, Button, Listbox, END, SINGLE

def load_key_mappings():
    with open('key_mappings.yaml', 'r') as file:
        return yaml.safe_load(file)

def save_key_mappings(mappings):
    with open('key_mappings.yaml', 'w') as file:
        yaml.dump(mappings, file)

def add_mapping(app_name, button1, button2, button3, knob_press, knob_cw, knob_ccw):
    mappings = load_key_mappings()
    mappings[app_name] = {
        'button1': button1,
        'button2': button2,
        'button3': button3,
        'knob_press': knob_press,
        'knob_cw': knob_cw,
        'knob_ccw': knob_ccw
    }
    save_key_mappings(mappings)

def delete_mapping(app_name):
    mappings = load_key_mappings()
    if app_name in mappings:
        del mappings[app_name]
        save_key_mappings(mappings)

def create_gui():
    root = Tk()
    root.title("Key Mappings Manager")

    Label(root, text="Application Name").grid(row=0, column=0)
    app_name_entry = Entry(root)
    app_name_entry.grid(row=0, column=1)

    Label(root, text="Button 1").grid(row=1, column=0)
    button1_entry = Entry(root)
    button1_entry.grid(row=1, column=1)

    Label(root, text="Button 2").grid(row=2, column=0)
    button2_entry = Entry(root)
    button2_entry.grid(row=2, column=1)

    Label(root, text="Button 3").grid(row=3, column=0)
    button3_entry = Entry(root)
    button3_entry.grid(row=3, column=1)

    Label(root, text="Knob Press").grid(row=4, column=0)
    knob_press_entry = Entry(root)
    knob_press_entry.grid(row=4, column=1)

    Label(root, text="Knob CW").grid(row=5, column=0)
    knob_cw_entry = Entry(root)
    knob_cw_entry.grid(row=5, column=1)

    Label(root, text="Knob CCW").grid(row=6, column=0)
    knob_ccw_entry = Entry(root)
    knob_ccw_entry.grid(row=6, column=1)

    def add_mapping_action():
        add_mapping(
            app_name_entry.get(),
            button1_entry.get(),
            button2_entry.get(),
            button3_entry.get(),
            knob_press_entry.get(),
            knob_cw_entry.get(),
            knob_ccw_entry.get()
        )
        refresh_listbox()

    def delete_mapping_action():
        selected_app = listbox.get(listbox.curselection())
        delete_mapping(selected_app)
        refresh_listbox()

    Button(root, text="Add Mapping", command=add_mapping_action).grid(row=7, column=0)
    Button(root, text="Delete Mapping", command=delete_mapping_action).grid(row=7, column=1)

    listbox = Listbox(root, selectmode=SINGLE)
    listbox.grid(row=8, column=0, columnspan=2)

    def refresh_listbox():
        listbox.delete(0, END)
        mappings = load_key_mappings()
        for app in mappings:
            listbox.insert(END, app)

    refresh_listbox()
    root.mainloop()

if __name__ == "__main__":
    create_gui()
