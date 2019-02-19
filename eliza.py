#!/usr/bin/python3

import re
import string
import random
import json
import sys 
import time
import colorama



def load_rules(filename, verbose=False):
    if verbose:
        print(f"Loading rules from {filename}. ", end="")
    
    with open(filename, "r") as f:
        data = [(p, t) for p, t in json.load(f)]
    
    if verbose:
        print("Done!")
    return data



def clean_up(s):
    s = re.split(r"\.|\?|;|!|(but)", s)[0]
    s = s.lower().strip(string.punctuation)
    s = re.sub("(good)?bye", "quit", s)
    return s



def demo(preprocess_rules, transformations, postprocess_rules):
    raise NotImplementedError 



def process(response, ruleset):
    for pat, sub in ruleset:
        response = re.sub(pat, sub, response)
    response = re.sub(r'\s+', ' ', response)
    return response



def transform(response, transformations):
    if response == "":
        response = "EMPTY"
    for pat, sub in transformations:
        pat = re.compile(pat)
        if re.search(pat, response):
            response = re.sub(pat, random.choice(sub), response)
            break
    return response



def respond(response, preprocess_rules, transformations, postprocess_rules):
    response = process(response, preprocess_rules)
    response = transform(response, transformations)
    response = process(response, postprocess_rules)

    response = response[0].upper() + response[1:]

    return response


def main(botname="eliza"):
    
    
    print(f"Loading rules for {botname}.")

    """preprocess_rules = load_rules(botname + ".preprocess.json", verbose=True)
    print("Preprocessing rules loaded.")

    postprocess_rules = load_rules(botname + ".postprocess.json", verbose=True)
    print("Postprocessing rules loaded.")

    transformations = load_rules(botname + ".transformations.json", verbose=True)
    print("Transformations loaded.")

    greetings = dict(load_rules(botname + ".greetings.json"))
    print("Greetings loaded.")
    prolog = greetings["prolog"]
    epilog = greetings["epilog"]"""

    filename = botname + '.json'
    with open(filename, 'r') as rulefile:
        rules_dict = json.load(rulefile)
    
    preprocess_rules = [(pat, rep) for (pat, rep) in rules_dict["preprocess_rules"]]
    postprocess_rules = [(pat, rep) for (pat, rep) in rules_dict["postprocess_rules"]]
    transformations = [(pattern, ruleset) for (pattern, ruleset) in rules_dict["transformations"]]
    prolog = rules_dict["prolog"]
    epilog = rules_dict["epilog"]

    
    for line in prolog:
        print(line)
    
    transcript = []
    comment = ""
    while True:
        comment = input("> ")
        transcript.append(comment)

        response = clean_up(comment)

        if response == "quit":
            break
        elif response == "demo":
            demo(preprocess_rules, transformations, postprocess_rules)
            break
        elif response == "post":
            print("\nPostprocessing Rules")
            for a, b in postprocess_rules:
                print(f"\t{a} => \"{b}\"")
            print("\n")
            transcript = transcript[:-1]
        elif response == "pre":
            print("\nPreprocessing Rules")
            for a, b in preprocess_rules:
                print(f"\t{a} => \"{b}\"")
            print("\n")
            transcript = transcript [:-1]
        elif response == "transformations":
            print("\nTransformations:")
            for a, b in transformations:
                print(f"\t{a} =>")
                for t in b:
                    print(f"\t\t{t}")
            transcript = transcript[:-1]
        elif response == "transcript":
            print("\nTranscript")
            for line in transcript:
                print('\t' + line)
            print("\n")
        else:
            response = respond(response, preprocess_rules, transformations, postprocess_rules)
        
        

        
        transcript.append(response)
        print(response)

    for line in epilog:
        print(line)
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = botname + "_transcript_" + timestr + ".txt"
    with open(filename, "w") as f:
        for line in transcript:
            f.write(line + "\n")
    
    print(f"A transcript of this sesson has been saved as {filename}.")


    


if __name__ == "__main__":
    colorama.init() # For running bots in Windows that use colorama to colorize text

    for arg in sys.argv[1:]:
        if arg in ["--help", "-h"]:
            print("""
Usage: ./eliza.py [-h] [bot=...]
    -h          Print out this help message
    bot=NAME    Load the files for the bot with name=NAME.
                If no name is specified, default to "eliza".

                For a bot to work, the following files must be in the same
                directory as eliza.py:
                    NAME.json
                
                If NAME.json does not exist, but NAME_rules.py does,
                then the NAME.json file may be created by running NAME_rules.py
            """)
            exit()

    botname = ""
    for arg in sys.argv:
        if len(arg) > 4 and arg[0:4] == "bot=":
            botname = arg[4:]
    
    botname = "eliza" if botname == "" else botname


    main(botname)