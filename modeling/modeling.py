
from transformers import pipeline
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("yhavinga/t5-v1.1-large-dutch-cnn-test")
model = AutoModelForSeq2SeqLM.from_pretrained("yhavinga/t5-v1.1-large-dutch-cnn-test")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

dir = "nl_txt"
def summarize(filename):
    try:
        with open(os.path.join(dir, filename.replace(".pdf","_NL.txt"))) as f:
            return summarizer(f.read())
    except:
        return None
df = pd.read_csv('cla.csv')
df["summary"]= df["filename"].apply(summarize)
df.to_csv('cla_with_summary.csv')




