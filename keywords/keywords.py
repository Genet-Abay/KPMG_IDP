import yake

kw_extractor = yake.KeywordExtractor()
dir = "nl_txt"

def tekst():
    try:
        with open(os.path.join(dir, filename.replace(".pdf","_NL.txt"))) as f:
            text=f.read()
            return text
    except:
        return None

def keywords(tekst):
    language = "nl"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(tekst)
    for kw in keywords:
        print(kw)
    df = pd.read_csv('cla.csv')
    df["keywords"]= df["filename"].apply(summarize)
    df.to_csv('cla_with_summary.csv')


