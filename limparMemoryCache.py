import os
import shutil
import tempfile
import tkinter as tk
from tkinter import messagebox

def delete_files_in_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Erro ao deletar o arquivo {file_path}: {e}')

def clean_cache():
    confirm = messagebox.askquestion("Confirmação", "Tem certeza de que deseja limpar a memória cache?")
    if confirm != 'yes':
        messagebox.showinfo("Cancelado", "Operação cancelada.")
        return

    success = False

    temp_directories = [tempfile.gettempdir(), 'C:\\Windows\\Temp']
    for temp_directory in temp_directories:
        delete_files_in_directory(temp_directory)
        success = True

    if success:
        prefetch_directory = 'C:\\Windows\\prefetch'
        delete_files_in_directory(prefetch_directory)
        messagebox.showinfo("Sucesso", "A pasta Prefetch foi limpa com sucesso!")


window = tk.Tk()
window.withdraw() 
clean_cache()
window.destroy()