import dearpygui.dearpygui as dpg


def callback(sender, app_data):
    file_name = f'{app_data["current_path"]}\\{app_data["file_name"]}'
    dpg.add_text(file_name, parent="Primary Window")


def cancel_callback(sender, app_data):
    print('Cancel was clicked.')
    print("Sender: ", sender)
