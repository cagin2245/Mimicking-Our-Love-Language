from parser import read_data, sanitize_messages
from NER import apply_ner, filter_messages

if __name__ == "__main__":    
    dir = input("Lütfen veri dosyasının konumunu giriniz (varsayılan: C:\\Users\\cagin\\Desktop\\New folder\\data.txt): ")
    if not dir.strip():
        dir = "C:\\Users\\cagin\\Desktop\\New folder\\data.txt"

    messages , author = read_data(loc = dir)

    sanitized_messages = sanitize_messages(messages)
    
    # Her mesaja NER uygula
    filter_message = []
    for text in sanitized_messages["i"]:
        ents = apply_ner(text)
        filter_message.append({"text": text, "ents": ents})

    ankara = filter_messages(filter_message, label="LOC", query="ankara", min_score=0.7)

    print(ankara)