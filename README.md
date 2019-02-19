# Eliza
This is Homework #1 for CSCI 538 with Dr. El-Ariss.

Eliza may be run by navigating to its parent folder and entering `./eliza.py` in Linux or `python eliza.py` in Windows.

By default, Eliza will load tranasformation rules from eliza.json. Rules for another file may be loaded by typing `bot=BOTNAME`, where `BOTNAME` is the name of the bot to be loaded, for which a BOTNAME.json file exists. For example, to load the included Groot example, run `./eliza.py bot=groot`.

If a bot's json file does not exist but a `BOTNAME_rules.py` file exists, then the `BOTNAME.json` file can be recreated by running `BOTNAME_rules.py`. Additional bots can be created easily by following the example of `eliza_rules.py` and `groot_rules.py`. To be a valid bot definition, `BOTNAME.json` must contain a JSON object/Python dictionary consisting of the following:
* **prolog**: A list of strings to be printed out before the conversation starts
* **preprocessing_rules**: A list of tuples consisting of a pattern to match, and replacements for it, for example:

      [(r"\bi'm\b", "i am"),
      (r"\b(can't)|(can not)\b", "cannot")]
  
  Preprocess Rules are run before text transformations.
     
* **transformations**: A list of tuples consisting of:
  1. A pattern to match
  2. A list of response strings.
  
  For example:
  
      (r"(.*\b)(name)(\b.*)",
          ["Great, good to know that.",
          "I am not interested in names."])
* **postprocess_rules**: Like the preprocess rules, but run after preprocess rules and transformations.
* **epilog**: A list of strings to be printed after the conclusion of the conversation, before the transcript is saved.
