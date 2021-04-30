## story 01
	*greet
		- utter_greet
## story 02
	*goodbye
		- utter_goodbye
## story 03
	*inform feature
		- action_inform_feature
## story 04
        *inform configuration
		- action_inform_configuration
## story 05
	*personal description
		- utter_personal_description
## Generated Story 2287634939685886640
* greet
    - utter_greet
* personal description
    - utter_personal_description
* inform configuration{"feature type": "trust mode", "configuration": "cli"}
    - slot{"configuration": "cli"}
    - slot{"feature type": "trust mode"}
    - action_inform_configuration
* inform feature{"feature type": "rate limit"}
    - slot{"feature type": "rate limit"}
    - action_inform_feature
    - slot{"feature type": "rate limit"}
* goodbye
    - utter_goodbye
* inform feature
    - utter_ask_feature
* inform feature
    - action_inform_feature
    - slot{"feature type": "rate limit"}
* inform configuration{"feature type": "schedule profile", "configuration": "syntax"}
    - slot{"configuration": "syntax"}
    - slot{"feature type": "schedule profile"}
    - action_inform_configuration
* inform configuration
    - utter_ask_configuration

