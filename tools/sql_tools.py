import sqlalchemy as alch
import os
import dotenv
import string
import spacy
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob








dotenv.load_dotenv()

passw = os.getenv("pass_sql")
dbName = "scripts_sentiment"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)




def personajes():
    query = list(engine.execute("SELECT personaje FROM scripts_sentiment.personajes;"))
    lista =  [{"personaje": elemento[0]} for elemento in query]
    return lista

def dialogos():
    query1=list(engine.execute("SELECT dialogo FROM scripts_sentiment.dialogos;"))
    lista1 =  [{"dialogo": elemento[0]} for elemento in query1]
    return lista1

def dialogo_persona(personaje):
    query2=list(engine.execute("SELECT dialogo FROM scripts_sentiment.dialogos WHERE Personaje = personaje;"))  
    lista2 =  [{"dialogo": elemento[0]} for elemento in query2]
    return lista2

def nuevomensaje(frase,personaje, tempo):
    engine.execute(f"""
    INSERT INTO dialogos (dialogo, personaje, temporada)
    VALUES ({frase}, '{personaje}', '{tempo}');
    """)
    
    return f"Se ha introducido correctamente: {frase}, {personaje}, {tempo}"
    
    