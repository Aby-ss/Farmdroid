from rich import box
from rich import print
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console

print("""
███████╗ █████╗ ██████╗ ███╗   ███╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
█████╗  ███████║██████╔╝██╔████╔██║██║  ██║██████╔╝██║   ██║██║██║  ██║
██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║██║  ██║██╔══██╗██║   ██║██║██║  ██║
██║     ██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
""")

print(Panel.fit("This is Farmdoid, A general purpose A.I made for the agriculture industry and general farms", title = " Farmdroid ", title_align = "left", box = box.SQUARE, border_style = "bold white"))

layout = Layout()
console = Console()

layout.split_column(
    Layout(name = "upper", size = 3),
    Layout(name = "body"),
    Layout(name = "footer", size = 3)
)

layout["body"].split_row(
    Layout(name = "Left"),
    Layout(name = "Right")
)

layout["Right"].split(Layout(name="box1"), Layout(name="box2"))

def Left_layout():
    left_p = Panel("""We established a company to give services that would improve the farmers' experience and provide a better control centre from them.They can use this to automate tedious and repetitive jobs that can be easily automated with the use of low-cost general-purpose A.I and robots. This can increase a farm's productivity while also increasing earnings and production capacities. \n\n\n\n\n\n     ______                         __           _     __
   / ____/___ __________ ___  ____/ /________  (_)___/ /
  / /_  / __ `/ ___/ __ `__ \/ __  / ___/ __ \/ / __  / 
 / __/ / /_/ / /  / / / / / / /_/ / /  / /_/ / / /_/ /  
/_/    \__,_/_/  /_/ /_/ /_/\__,_/_/   \____/_/\__,_/   
                                                        
                                                        
This is the main command and control centre for your garden or farm. You may see many statistics about your land. On the left, you can view the camera readings and everything it detects. A chat bot can also be used to read and evaluate specific things.""", title = " F A R M D O I D ", title_align = "left", border_style = "bold", box = box.SQUARE)

    return left_p

layout["Left"].update(Left_layout())
print(layout)