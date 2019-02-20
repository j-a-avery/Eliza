# Eliza
This is Homework #1 for CSCI 538 with Dr. El-Ariss.

Eliza may be run by navigating to its parent folder and entering `./eliza.py` in Linux or `python eliza.py` in Windows.

By default, Eliza will load tranasformation rules from eliza.json. Rules for another file may be loaded by typing `bot=BOTNAME`, where `BOTNAME` is the name of the bot to be loaded, for which a BOTNAME.json file exists. For example, to load the included Groot example, run `./eliza.py bot=groot`.

If a bot's json file does not exist but a `BOTNAME_rules.py` file exists, then the `BOTNAME.json` file can be recreated by running `BOTNAME_rules.py`. Additional bots can be created easily by following the example of `eliza_rules.py` and `groot_rules.py`.

To be a valid bot definition, `BOTNAME.json` must contain a JSON object/Python dictionary consisting of the following:
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

## Sample Session

A sample Eliza session is as follows. (The user's intereactions are in *italics*, and Eliza's are `formatted as code`.)

*Men are all alike.*

`What similarities are there?`

*They're always bugging us about something or other.*

`What incident are you thinking of?`

*Well, my boyfriend made me come here.*

`Your boyfriend made you come here?`

*He says I am depressed much of the time.*

`I am sure it's not pleasant to be sad.`

*It's true, I am unhappy.*

`Do you want to be unhappy?`

*I need some help; that much seems certain.*

`What would it mean to you if you got some help?`

*Perhaps I could learn to get along with my mother.*

`Who else in your family ?`

*My mother takes care of me.*

`Who else in your family takes care of you?`

*My father.*

`Your father?`

*You are like my father in some ways.*

`Does he influence you strongly?`

*You are not very aggressive, but I think you don't want me to notice that.*

`What makes you think I am not very aggressive, ?`

*You don't argue with me.*

`Why do you think I don't argue with you?`

*You are afraid of me.*

`What makes you think I am afraid of you?`

*My father is afraid of everybody.*

`Your father?`

*quit*
