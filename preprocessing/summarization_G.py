from transformers import pipeline


def summarize(file_name):
    """
    this function summarizes text in the given function and return summarized text to the caller
    """
    with open(file_name, 'r') as f:
        text = file_name.read()    
        summarizer = pipeline("summarization")
        summarized = summarizer(text, min_length=5, max_length=10)  
    f.close() 
    return summarized    


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