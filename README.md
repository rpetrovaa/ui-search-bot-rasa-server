This project contains the Rasa Server configuration for UI Search Bot, including NLU and DM.

The set of training examples to the intents can be found in nlu.yml.
The rules for DM are in rules.yml. The pipeline config is in config.yml.
Slots and entities are defined in file domain.yml
The request tracking global query and request payload, that are forwarded to the Angular chatbot web app, are processed in file ./actions/actions.py.

To run the Rasa Server you need to have Rasa installed locally. For installing Rasa go to https://rasa.com/docs/rasa/installation/.

Once you have Rasa installed, you need to create a conda environment, where you can run the project.

The command for starting the Rasa server is: rasa run -m models --enable-api --cors "<asterix>" --debug
Make sure to insert the icon for <asterix> instead of the tag

In addition to the Rasa main Server you need to start the Custom Actions server. You can run Rasa Custom Actions with the following command: rasa run actions
