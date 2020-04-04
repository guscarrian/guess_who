
 

## negative path
* greet
  - utter_greet
* mood
  - utter_play_game
* deny
  - utter_goodbye


## affirmative_incomplete  path
* greet
  - utter_greet
* mood
  - utter_play_game
* affirm 
  - utter_game_intro
  - utter_start
* deny
  - utter_goodbye

## affirmative path
* greet
  - utter_greet
* mood
  - utter_play_game
* affirm
  - utter_game_intro
  - utter_start
* affirm
  - utter_characters
  - utter_ready
*user_answers
  - action_user_answers


## custom user_answers actions
#*user_answers
#  - action_user_answers

