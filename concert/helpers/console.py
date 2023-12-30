import os, time
from rich.console import Console
from rich.progress import track
from rich.table import Table


console = Console()

def clear_output():
    os.system('clear')
    
def success_msg(pesan_berhasil):
    clear_output()
    console.print(f"SUCCESS: {pesan_berhasil}", style='bold green')
    time.sleep(2)
    
def error_msg(pesan_error):
    clear_output()
    console.print(f"ERROR: {pesan_error}", style='bold red')
    time.sleep(2)
    
def loading():
    for _ in track(range(1), description="Memproses..."):
        time.sleep(1)

def tabel(title, data):
    tbl_konser = Table(title=title)
    columns = []
    for column in data[0].keys():
        tbl_konser.add_column(column, style="bold dark_olive_green3", no_wrap=True)
        columns.append(column)
    for row in data:
        content_row = []
        for column in columns:
            content_row.append(str(row[column]))
        tbl_konser.add_row(*content_row)
    return tbl_konser