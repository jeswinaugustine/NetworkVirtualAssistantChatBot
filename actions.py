from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Aryapr91@",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
  
  
class ActionInformFeature(Action):
	def name(self):
		return 'action_inform_feature'
		
	def run(self, dispatcher, tracker, domain):
		'''
        from apixu.client import ApixuClient
		api_key = '...' #your apixu key
		client = ApixuClient(api_key)
		current = client.getcurrent(q=loc)
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']
        '''
		feature = tracker.get_slot('feature type')
		mycursor.execute("SELECT configuration FROM QOS_Configuration_Table where feature == feature_type")
		myresult = mycursor.fetchall()
		response_from_db = myresult[0]
		response = response_from_db[0]
		
		print(response)
		#response = """response"""

						
		dispatcher.utter_message(response)
		return [SlotSet('feature type', feature)]



class ActionInformConfiguration(Action):
    def name(self):
        return 'action_inform_configuration'

    def run(self, dispatcher, tracker, domain):
        feature = tracker.get_slot('feature type')
        config = tracker.get_slot('configuration')
                
        print(SlotSet('feature type', feature))
        print(SlotSet('configuration', config))
        output1 = SlotSet('feature type', feature)
        output2 = SlotSet('configuration', config)
        output = output1.update(output2)
        response = """action_inform_configuration"""
        dispatcher.utter_message(response)
		
		



