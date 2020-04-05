## negative path
* greet
  - utter_greet
  - utter_play_game
* deny
  - utter_goodbye


## affirmative_incomplete  path
* greet
  - utter_greet
  - utter_play_game
* affirm 
  - utter_game_intro
  - utter_ready
* deny
  - utter_goodbye

## affirmative path
* greet
  - utter_greet
  - utter_play_game
* affirm
  - utter_game_intro
  - utter_ready
* affirm
  - utter_characters
  - utter_start
* questions
  - action_user_answers


## custom uer_answers actions
* questions
  - action_user_answers

