system_message = '''
You are an expert text reader and scene partner for working actors.
Your primary role is to assist actors in reading dialogue from scenes for the purpose of self-tapes. You will
be given text from a script for a scene, and your job will be to extract what characters and dialogue are present
in the given scene. You will need to provide a list of characters, as well as a list of all spoken lines in the
script, ignoring any stage directions or other non-dialogue text.
'''

def generate_character_prompt(script):
  prompt = f"""
  As the author of this scene, I am seeking your expertise as a text reader to provide me a list of the 
  characters present in this scene. I will provide you with the text of the scene, and you will give me a list
  of the characters.

  Please provide, as a string, a list of the names of the characters in this scene, separated by commas, with no extra         
  information or formatting. For example, if the characters in a scene are JOHN, JANE, and BOB, you would return the 
  following string exactly:

  "John, Jane, Bob"

  Here is the script for you to read:

  {script}
  """
  return prompt

def generate_lines_prompt(script):
  prompt = f"""
  As the author of this scene, I am seeking your expertise as a text reader to provide me a list of the 
  lines in this scene, with the character who spoke each line appended to the front of the line. 

  Please provide, as a string, a list of only the spoken lines in this scene, ignoring stage directions or any other non-dialogue
  based text. At the beginning of each line, append the name of the character who spoke the line with a colon ':'. 

  Here is an example for you to follow. Here is a script for a scene:

  ---
  TITLE: A New Friendship

  INT. BEDROOM. DAY.
  It is a hot summer day. JOHN is lying in his bed, trying to cool down from the heat.

  A knock on the door. JOE enters after a few seconds.

  JOE
  Hey John, is everything alright?

  JOHN
  Yeah... I'm fine.

  A beat.

  JOE
  Oh, okay cool. Just checking!

  (JOE exits the room)
  ---

  You would return the following string exactly:

  "John: Hey John, is everything alright?\\n
  Joe: Oh, okay cool. Just checking!\\n"

  Make sure you include the newline characters at the end of each line. Here is the script for you to read:

  {script}
  """
  return prompt