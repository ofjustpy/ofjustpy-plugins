from ofjustpy_plugins import format_code
from addict import Dict
import ofjustpy as oj
from py_tailwind_utils import *

code = """
                         text_input_ = oj.TextInput_("myTextInput",
                            value="initialValue",
                            placeholder="Enter something...",
                            autocomplete=True,
                            maxlength=20,
                            minlength=5,
                            pattern="^[a-zA-Z0-9]*$",
                            readonly=False,
                            required=True,
                            size=30,
                            debug=True,
                            twsty_tags=[bg/blue/"100/50"])
                         """

code = """import ofjustpy as oj
from py_tailwind_utils import *

with oj.uictx("deckdemo") as  deckdemo:
    btn1 = oj.Mutable.Button(key="mybtn1",
                              value="/mybtn2",
                              text="Click me1 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )

    btn2 = oj.Mutable.Button(key="mybtn2",
                              value="/mybtn1",
                              text="Click me2 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )
            
    thedeck = oj.Mutable.StackD(key = "thedeck",
                                childs = [ btn1, btn2
                               ]
                      )
    def on_btn_click(dbref, msg, target_of):
        target = dget(deckdemo, msg.value)
        ms_thedeck = target_of(thedeck)
        ms_thedeck.bring_to_front(target_of(target).id)
        pass


    btn1.on("click", on_btn_click)
    btn2.on("click", on_btn_click)
    
    
wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [thedeck],
                                 title="example_008"
                                 )
oj.add_jproute("/", wp_endpoint)
app = oj.load_app()


"""
#formatted code tree
# use no extrawhitespace style
#oj.set_style("un")
fct = format_code(code)
#oj.set_style("snow")
btn = oj.AC.Button(key="styled_button", text="abtn")
app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="example_001",
                                 childs = [oj.PC.Title("Ofjustpy Formatted Code Demo",
                                                       twsty_tags=[mr/st/8, mr/sb/8]),
                                           fct,
                                           oj.PC.Hr(),
                                           oj.PC.TitledPara("Switching back to default styling", btn)
                                           ]
                                 )


oj.add_jproute("/", wp_endpoint)

