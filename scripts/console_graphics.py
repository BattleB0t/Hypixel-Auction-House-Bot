#I know the code is awful-
from rich import markdown
from rich.console import Console
from rich.markdown import Markdown

import os

console = Console()

def clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        os.system('clear')
    else:
      # for windows platfrom
        os.system('cls')

def md_print(MarkdownString):
    console.print(Markdown(MarkdownString))

def format_markdown(header, sub_headers, list_items): #List items are 2d arrays with each incriment in the y-axis being another sub_header.
    clear()

    md_print(f"""# {header}""")

    sub_header_incrimentor = 0
    for sub_header in sub_headers:
        md_print(f"""## {sub_header}""")

        item_incrimentor = 0
        for item in list_items[sub_header_incrimentor]:
            item_incrimentor += 1
            md_print(f"""{item_incrimentor}. {item}""")
