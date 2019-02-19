#!/usr/bin/python3

import re, string, json

prolog = [
     '\n\nHello! Please state your problem.',
     "Please say \"quit\" or \"goodbye\" when you are ready to conclude our session."
]

preprocess_rules = [
     (f"{re.escape(string.punctuation)}", ''),
     (r"\bi'm\b", "i am"),
     (r"\b(can't)|(can not)\b", "cannot"),
     (r"\b(you're)|(youre)\b", "you are"),
     (r"^((you )?see|well|um+)\b", ""),
     (r"\b(sort|kind)a\b", ""),
     (r"\b(sort|kind)\s*of\b", "")
]

transformations = [    
     (r"(.*\b)(hi|hello|howdy|greetings|hola)(\b.*)",
          ["Hi there. Please state 2PP problem."]),
          
     (r"(.*\b)(b[^a-h^j-z]tch|d[^b-z]mn|f[^a-t^v-z]ck|sh[^a-h^j-z]t|[^b-z]ss)(\b.*)",
         ["That must be very upsetting for 2PNA.",
          "I would appreciate it if 2PNA wouldn't swear.",
          "I can see 2PP frustration."]),
    
    (r"(.*\b)(name)(\b.*)", 
         ["Great, good to know that.",
          "I am not interested in names."]),
    
    (r"(.*\b)(sorry)(\b.*)",
         ["Please don't apologize.",
          "Apologies BE.PL not necessary.",
          "What feelings do 2PNA have when 2PNA apologize?"]),
    
    (r"(?P<subj>.*?)(\bi remember\b)(?P<pred>.*)",
         [r"Do 2PNA often think of \g<pred>?",
          r"Does thinking of \g<pred> bring anything else to mind?",
          "What else do 2PNA remember?",
          r"Why do 2PNA recall \g<pred> right now?"]),
    
    (r"(?P<subj>.*?)(\bif\b)(?P<pred>.*)",
         [r"Do 2PNA really think it is likely that \g<pred>?",
          r"Do 2PNA wish that \g<pred>?",
          r"What do 2PNA think about \g<pred>",
          r"Really--if \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(?P<dream>dream(ed)? about)(?P<pred>\b.*)",
         [r"How do 2PNA feel about \g<pred> in reality?"]),
    
    (r"(?P<subj>.*\b)(?P<dream>dream(ed)?)(?P<pred>\b.*)",
         [r"Really -- \g<pred>?",
          "What does this dream suggest to 2PNA?",
          "Do 2PNA dream often?",
          r"Have 2PNA dreamed \g<pred> before?"]),
    
    (r"(?P<subj>.*\b)(my mother|mom|mama)(?P<pred>\b.*)",
         [r"Who else in 2PP family \g<pred>?",
          "Tell 1PA more about 2PP family."]),
    
    (r"(?P<subj>.*\b)(my father|dad|daddy|papa)(?P<pred>\b.*)",
         ["Your father?",
          "Does he influence 2PNA strongly?",
          "Tell 1PA more about 2PP family."]),

    (r"(?P<subj>.*\b)(my)(?P<pred>\b.*)",
        [r"2PP \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(i want)(?P<pred>\b.*)",
         [r"What would it mean for 2PNA if 2PNA got \g<pred>?",
          r"Why do 2PNA want \g<pred>?",
          r"Suppose 2PNA got \g<pred> soon. What then?"]),
    
    (r"(?P<subj>.*\b)(i need)(?P<pred>\b.*)",
         [r"What would it mean to 2PNA if 2PNA got \g<pred>?"]),

    (r"(?P<subj>.*\b)(i think)(?P<pred>\b.*)",
        [r"What makes 2PNA think \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(i am glad)(?P<pred>\b.*)",
         [r"How have 1PN helped 2PNA to be \g<pred>?",
          "What makes 2PNA happy just now?",
          r"Can 1PN explain why 2PNA BE.PL suddenly happy \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(i am sad about)(?P<pred>\b.*)",
         [r"Why does \g<pred> make 2PNA sad?"]),
    
    (r"(?P<subj>.*\b)(i am sad|depressed)(?P<pred>\b.*)",
         ["1PN am sorry to hear 2PNA BE.PL depressed.",
          "1PN am sure it's not pleasant to be sad.",
          r"Why does \g<pred> make 2PNA sad?"]),
    
    (r"(?P<subj>.*\b)(are like)(?P<pred>\b.*)",
         [r"What resemblance do 2PNA see between \g<subj> and \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(is like)(?P<pred>\b.*)",
         [r"In what way is it that \g<subj> is like \g<pred>?",
          "What resemblance do 2PNA see?",
          "Could there really be some connection?"]),
    
    (r"(?P<subj>.*\b)(alike)(?P<pred>\b.*)",
         ["In what way?", 
          "What similarities BE.PL there?"]),
    
    (r"(?P<subj>.*\b)(same)(?P<pred>\b.*)",
         ["What other connections do 2PNA see?"]),
    
    (r"(?P<subj>.*\b)(i was)(?P<pred>\b.*)",
         ["Were 2PNA really?",
          r"Why do 2PNA tell me 2PNA were \g<pred> now?"]),
    
    (r"(?P<subj>.*\b)(i am)(?P<pred>\b.*)", 
         [r"In what way BE.PL 2PNA \g<pred>?",
          r"Do 2PNA want to be \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(am i)(?P<pred>\b.*)", 
         [r"Do 2PNA believe 2PNA BE.PL \g<pred>?",
          r"Would 2PNA want to be \g<pred>?",
          r"YDo you wish 1PN would tell 2PNA 2PNA BE.PL \g<pred>?",
          r"What would it mean if 2PNA were \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(you are)(?P<pred>\b.*)", 
         [r"What makes 2PNA think 1PN am \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(you)(?P<pred>\b.*)(i|me.*)",
         [r"Why do 2PNA think 1PN \g<pred> 2PNA?"]),
    
    (r"(?P<subj>.*\b)(because)(?P<pred>\b.*)",
         ["Is that the real reason?",
          "What other reasons might there be",
          "Does that reason seem to explain anything else?"]),
    
    (r"(?P<subj>.*\b)(were you)(?P<pred>\b.*)",
         [r"Perhaps 1PN was \g<pred>",
          "What do 2PNA think?",
          r"What if 1PN had been \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(i cannot)(?P<pred>\b.*)",
         [r"Maybe 2PNA could \g<pred> now.",
          r"What if 2PNA could \g<pred>"]),
    
    (r"(?P<subj>.*\b)(i feel)(?P<pred>\b.*)",
         [r"Do 2PNA often feel \g<pred>?"]),
    
    (r"(?P<subj>.*\b)(i felt)(?P<pred>\b.*)",
         ["What other feelings do 2PNA have?"]),
    
    (r"(?P<subj>.*\b)(why don't you)(?P<pred>\b.*)",
         [r"Should 2PNA \g<pred> 2PR?",
          r"Do 2PR believe 1PN don't \g<pred>?",
          r"Perhaps 1PN will \g<pred> in good time."]),
    
    (r"(?P<subj>.*\b)(ye([sp]|ah))(?P<pred>\b.*)",
         ["You seem quite positive.",
          "Are 2PNA sure?",
          "1PN see."]),
    
    (r"(?P<subj>.*\b)(?P<neg>no(pe)?)(?P<pred>\b.*)",
         ["You BE.PL being a bit negative, aren't 2PNA?",
          r'Are 2PNA saying "\g<neg>" just to be negative?']),
    
    (r"(?P<subj>.*\b)(someone|somebody)(?P<pred>\b.*)",
         ["Can 2PNA be more specific?"]),
    
    (r"(?P<subj>.*\b)(everyone|everybody)(?P<pred>\b.*)",
         ["Can 2PNA think of anyone in particular?",
          "Who, for example?"]),
    
    (r"(?P<subj>.*\b)(always)(?P<pred>\b.*)",
         ["Can 2PNA think of a specific example?",
          "What incident BE.PL 2PNA thinking of?",
          "Really? Always?"]),
    
    (r"(?P<subj>.*\b)(maybe|perhaps)(?P<pred>\b.*)",
         ["You do not seem quite certain."]),
    
    (r"(?P<subj>.*\b)(are)(?P<pred>\b.*)",
         [r"Did 2PNA think they might not be \g<pred>?",
          r"Possibly they are \g<pred>"]),

    (r"^knock\s+knock.*$",
        [r"Who's there?"]),
    
    ("EMPTY|.+", [
            "Very intersting.",
            "I am not sure I understand 2PNA fully.",
            "Please contine.",
            "Do 2PNA feel strongly about discussing such things?"])]

postprocess_rules = [
    (r"BE.PL", "are"),
    (r"you are", "I am"),
    (r"\byou\b", "I"),
    (r"\bi\b", "you"),
    (r"\bme\b", "you"),
    (r"\bmy\b", "2PP"),
    (r"\byour\b", "my"),
    (r"\b2PP\b", "your"),
    (r"\byourself\b", "1PR"),
    (r"\bmyself\b", "yourself"),
    (r"\b2PR\b", "yourself"),
    (r"\b1PR\b", "myself"),
    (r"\b1PA\b", "me"),
    (r"\b1PN\b", "I"),
    (r"\b2PNA\b", "you"),
    (r"\bi\b", "I")
]

epilog = ["Goodbye! I hope our session was enlightening."]

greetings = [
     ("prolog", prolog),
     ("epilog", epilog)
]

script = {
     "prolog": prolog,
     "preprocess_rules": preprocess_rules,
     "transformations": transformations,
     "postprocess_rules": postprocess_rules,
     "epilog": epilog
}

with open("eliza.json", "w") as f:
     json.dump(script, f, indent=2)
