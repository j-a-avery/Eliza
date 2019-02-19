#!/usr/bin/python3

import json, colorama

prolog = [
    "If ya wanna talk to Groot, good luck.",
    "Ya can't understand a word he says.",
    "Be sure to tell \'im \"bye\" when you're done with \'im."
]

epilog = [
    "If ya wanna see whatcha said for some reason, just look at the transcript."
]

preprocess_rules = []
postprocess_rules = []

transformations = [    
     (r"(.*\b)(hi|hello|howdy|greetings|hola)(\b.*)",
          ["I am Groot."]),
          
     (r"(.*\b)(b[^a-h^j-z]tch|d[^b-z]mn|f[^a-t^v-z]ck|sh[^a-h^j-z]t|[^b-z]ss)(\b.*)",
         [f"{colorama.Style.BRIGHT}I! AM! GROOOOOOOT!{colorama.Style.NORMAL}"]),
    
    (r"(.*\b)(name)(\b.*)", 
         [f"I am {colorama.Style.BRIGHT}Groot{colorama.Style.NORMAL}."]),
    
    (r"(.*\b)(sorry)(\b.*)",
         [f"{colorama.Style.DIM}I am Groot....{colorama.Style.NORMAL}"]),

    (r"(?P<subj>.*\b)(i|my|me)(?P<pred>\b.*)",
        [f"{colorama.Style.BRIGHT}I{colorama.Style.NORMAL} am Groot."]),
    
    (r"(?P<subj>.*\b)(you)(?P<pred>\b.*)", 
         [f"I {colorama.Style.BRIGHT}am{colorama.Style.NORMAL} Groot."]),
    
    (r"(?P<subj>.*\b)(ye([sp]|ah))(?P<pred>\b.*)",
         [f"I am Groot!"]),
    
    (r"(?P<subj>.*\b)(?P<neg>no(pe)?)(?P<pred>\b.*)",
         ["I... am... Groot...."]),

    ("EMPTY|.+", [
            "I am Groot."])]

script = {
    "prolog": prolog,
    "preprocess_rules": preprocess_rules,
    "transformations": transformations,
    "postprocess_rules": postprocess_rules,
    "epilog": epilog
}

with open("groot.json", "w") as f:
    json.dump(script, f, indent=2)
