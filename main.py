#modules
import speech_recognition as SR
from pymongo import MongoClient
import pyttsx3
from pprint import pprint

class storenames:
            def get_audio(self):#function to get audio from user and convert it to text
                r=SR.Recognizer()
                with SR.Microphone() as source:
                    audio=r.listen(source,timeout=5)
                    said=""

                    try:
                        said=r.recognize_google(audio)
                    except Exception as e:
                        print("Exception:",str(e))

                return said.lower()

            def insertintoDB(self,text,db):#function to insert name into the database
                data={
                     'name':text
                }
                db.names.insert_one(data)


            def getallnames(self,db):#function to get all the names from the database
                data=db.names.find({},{'name':1,'_id':0})
                print("all stored names are:")
                for each in data:
                    print("* ",each["name"])



def main():

    client = MongoClient(port=27017)#default port of mongodb
    db = client.mydatabase_lib#selecting the database
    print("Program Started")
    storename=storenames()#initializing the class
    while True:
        print("Listening...")
        text=storename.get_audio()
        print(text)
        if text=="stop":#ending the program
            print("PROGRAM STOPPED")
            break
        elif text=="get all names":
            storename.getallnames(db)
        elif text!="":
            print("name is being inserted")
            storename.insertintoDB(text,db)





main()