Connect Rasa to and fetch data from MySql database

Python 3.8.18
Rasa 3.6.17

Define MySQL Connection Details

    Create a separate Python file (e.g., database_utils.py) to store database connection information

Create Custom Action

    In your actions.py file, define a custom action to query the database

Update NLU Training Data

    Include intents and entities in your nlu.yml file to capture user requests for database queries

Integrate Custom Action

    In your domain.yml file, link the query_database intent to the custom action


Train and Run

    Train your Rasa model using 
        ~ rasa train
    Start the bot with 
        ~ rasa run --enable-api

