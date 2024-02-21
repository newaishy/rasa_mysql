
from typing import Text, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.shared.core.events import SlotSet
from db_utils import get_db_connection  # Import from step 1
from typing import List


def action_query_database(
    user_id: Text,
    requested_data: Text,  # Slot to store user-requested data
    database_slot: Text = "database_response",  # Slot to store response 
    ) -> List[Dict[Text, Any]]:

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        # Construct SQL query based on user-requested data
        query = f"SELECT * FROM your_table WHERE your_column LIKE %s"
        cursor.execute(query, (f"%{requested_data}%",))

        results = cursor.fetchall()
        connection.close()

        # Format and store results in slot
        formatted_results = []
        for row in results:
            formatted_results.append({"data": row[0]})  # Customize formatting

        return [SlotSet(database_slot, formatted_results)]
    else:
        return []  # Handle errors or provide appropriate feedback
