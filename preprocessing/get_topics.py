import pandas as pd
import re
import re
import nltk
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

import spacy
from spacy.lang.nl.examples import sentences 
import lemminflect


df_cao = pd.read_csv(r"C:\BeCode\KPMG_data\CLA_meta_from_2018.csv")

df_cao = df_cao[df_cao['themes_nl'].notna()]


df_keywords = pd.read_excel(r"C:\BeCode\KPMG_data\Key_word.xlsx" , index_col=None, header=None)
new_header = df_keywords.iloc[0] 
df_keywords = df_keywords[1:]
df_keywords.columns = new_header 
df_keywords.head()


nltk.download('punkt')
def clean_text(text):
  text = text.lower()
  text = re.sub("[^a-zA-Z\'\-]", " ", text) 
  return " ".join(word_tokenize(text)[:256])

def get_topica(df_cao):

    nlp = spacy.load("nl_core_news_sm")
    stop_words = """
    swt excl er swe re le aanv aan af al alle alles allebei alleen allen als altijd ander anders andere anderen aangaande aangezien achter achterna
    afgelopen aldus alhoewel anderzijds ben bij bijna bijvoorbeeld behalve beide beiden beneden bent bepaald beter betere betreffende binnen binnenin boven
    bovenal bovendien bovenstaand buiten daar dan dat de der den deze die dit doch doen door dus daarheen daarin daarna daarnet daarom daarop des dezelfde dezen
    dien dikwijls doet doorgaand doorgaans een eens en er echter enige eerder eerst eerste eersten effe eigen elk elke enkel enkele enz erdoor etc even eveneens
    evenwel ff ge geen geweest gauw gedurende gegeven gehad geheel gekund geleden gelijk gemogen geven geweest gewoon gewoonweg
    geworden gij haar had heb hebben heeft hem het hier hij hoe hun hadden hare hebt hele hen hierbeneden hierboven hierin hoewel hun
    iemand iets ik in is idd ieder ikke ikzelf indien inmiddels inz inzake ja je jou jouw jullie jezelf jij jijzelf jouwe juist kan kon kunnen klaar konden krachtens kunnen kunt
    lang later liet liever maar me meer men met mij mijn moet mag mede meer meesten mezelf mijzelf min minder misschien mocht mochten moest moesten
    moet moeten mogelijk mogen na naar niet niets nog nu nabij nadat net nogal nooit nr nu
    of om omdat ons ook op over omhoog omlaag omstreeks omtrent omver onder ondertussen ongeveer onszelf onze ooit opdat
    opnieuw opzij over overigens pas pp precies prof publ reeds rond rondom sedert sinds sindsdien slechts sommige spoedig steeds
    ‘t 't te tegen toch toen tot tamelijk ten tenzij ter terwijl thans tijdens toe totdat tussen u uit uw uitgezonderd uwe uwen
    van veel voor vaak vanaf vandaan vanuit vanwege veeleer verder verre vervolgens vgl volgens vooraf vooral vooralsnog
    voorbij voordat voordien voorheen voorop voort voorts vooruit vrij vroeg
    want waren was wat we wel werd wezen wie wij wil worden waar waarom wanneer want weer weg wegens weinig weinige weldra
    welk welke welken werd werden wiens wier wilde wordt
    zal ze zei zelf zich zij zijn zo zonder zou zeer zeker zekere zelfde zelfs zichzelf zijnde zijne zo’n zoals zodra zouden
    zoveel zowat zulk zulke zulks zullen zult
    """.split()


    column_topic = []
    for index, row in df_cao.iterrows():       
        theme = row["themes_nl"]
        them = theme.replace('\\' ,'/' )
        thems = theme.split('/')
        
        sub_topic = []
        for t in thems:
            t = clean_text(t)
            toknized_word = word_tokenize(t)
            filtered_tokens = [w for w in toknized_word if not w.lower() in stop_words]
            sub_topic.append(' '.join(filtered_tokens))

        
        # for t in filtered_tokens:
        #     if t not in key_words:
        #         key_words.append()

        topics = '/ '.join(sub_topic)    
        column_topic.append(topics)

    df_cao['topics_found'] = column_topic
    df_cao.to_csv(r"C:\BeCode\KPMG_data\CLA_meta_from_2018_withtopics.csv")