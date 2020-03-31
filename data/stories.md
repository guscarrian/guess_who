 


## negative path
* greet
  - utter_greet
* mood
  - utter_play_game
* deny
  - utter_goodbye
* goodbye

## affirmative_incomplete  path
* greet
  - utter_greet
* mood
  - utter_play_game
* user_answers 
  - utter_game_intro
  - utter_start
* user_answers
  - utter_goodbye

## affirmative path
* greet
  - utter_greet
* mood
  - utter_play_game
* user_answers
  - utter_game_intro
  - utter_start
* user_answers
  - utter_characters
  - utter_ready
  - utter_question1

## custom user_answers actions
*user_answers
  - action_user_answers

