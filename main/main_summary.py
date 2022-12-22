import os
import pandas as pd
from preprocessing import pdf2text_pdfMminer
from preprocessing import split_languages
from preprocessing import summarization_G

def main():
    root_path = "C:/BeCode/KPMG_data/A/"
    df_cao_meta =  pd.read_csv("C:/BeCode/KPMG_data/CLA_meta_from_2018_withtopics.csv")
    df_cao_meta["summary"] = "None"
    for root, dirs, files in os.walk(root_path):      
        for  d in dirs:        
            for root2, dirs2, files2 in os.walk(os.path.join(root,d)): 
                for f in files2:  
                    text = pdf2text_pdfMminer.convert_pdf_to_txt(root_path)
                    nl_text = split_languages.split_file(text)
                    summary = summarization_G.summarize(nl_text)

                    file_name = os.path.basename(f)
                    df_cao_meta.loc[df_cao_meta['filename'] == file_name, 'summary'] = summary


if __name__ == "__main__":
    main