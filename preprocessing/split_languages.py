from langdetect import detect
from textblob import TextBlob
from googletrans import Translator
import os


translator = Translator()

def split_file(file_name):
    """
    this function splits the given text file in to nederlands and frech language and save the in file adding nl or fr 
    on the given file name
    """
    with open(file_name, 'r') as f:
        text = f.read()
        split_txt = text.split("\n\n")
        count = 0
        nl_text = []
        fr_text = []

        for line in split_txt:
            try:
                if detect(line) == 'nl':
                    nl_text.append()                    
                else:
                    fr_text.append()

            except:
                print("Error while detecting text:   " + line)
                continue

            # print()            
            # count+=1
            # if count>=30:
            #     break

        file_nl = open(file_name + '_nl' + '.txt', 'w')
        file_nl.write(' \n'.join(nl_text))

        file_fr = open(file_name + '_fr' + '.txt', 'w')
        file_fr.write(' \n'.join(fr_text))            

        f.close()
        file_fr.close()
        file_nl.close()


def main():
    root_path = "C:/BeCode/KPMG_data/A/"
    for root, dirs, files in os.walk(root_path):      
        for  d in dirs:        
            for root2, dirs2, files2 in os.walk(os.path.join(root,d)): 
                for f in files2:
                    split_file(f) 
        print(f"spliting for current sub folder  and file {f} is finished")
    print(f"spliting for current folder  and for a sub folder {dirs} is finished")

if __name__ == "__main__":
    main()
