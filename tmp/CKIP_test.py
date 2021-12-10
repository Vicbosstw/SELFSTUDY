from ckip_transformers import __version__
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker


def main():

    # Show version
    print(__version__)

    # Initialize drivers
    print("Initializing drivers ... WS")
    ws_driver = CkipWordSegmenter(level=3)
    print("Initializing drivers ... POS")
    pos_driver = CkipPosTagger(level=3)
    print("Initializing drivers ... NER")
    ner_driver = CkipNerChunker(level=3)
    print("Initializing drivers ... done")
    print()

    # Input text
    text = [
        "《民國趣史》共有二輯，第一輯初版於一九一五年三月，分有壽星集、遺老傳、官場瑣細、裙釵韻語、",
        "社會雜談等大類，第二輯初版於一九一七年五月，分有慶頌聲、榮哀錄、神怪談、續情史、新黑幕、博物院等大類。",
        "每大類中還有許多小題目，包羅萬象。文中所記載，多為作者當時所聞，上至達官顯要，下至市井小民，皆有入文。",
        "本書整合二輯內容，重新排版、點校。書中所記之名人趣談、奇聞軼事，可一窺當時在新與舊、",
        "中與西交相衝擊下的民初社會，所呈現出的各種光怪陸離樣貌。並可與正史相輔，為研究民初歷史之參考資料。",
        "李定夷，民初報人小說家，著作豐富。著有多本長、短篇小說，以及多篇隨文筆記。",
        "因其歷任多刊報紙與雜誌之編輯、主編，對於當時之社會現況有所了解與深思"
    ]

    # Run pipeline
    print("Running pipeline ... WS")
    ws = ws_driver(text)
    print("Running pipeline ... POS")
    pos = pos_driver(ws)
    print("Running pipeline ... NER")
    ner = ner_driver(text)
    print("Running pipeline ... done")
    print()

    # Show results
    for sentence, sentence_ws, sentence_pos, sentence_ner in zip(text, ws, pos, ner):
        print(sentence)
        print(pack_ws_pos_sentece(sentence_ws, sentence_pos))
        for entity in sentence_ner:
            print(entity)
        print()


# Pack word segmentation and part-of-speech results
def pack_ws_pos_sentece(sentence_ws, sentence_pos):
    assert len(sentence_ws) == len(sentence_pos)
    res = []
    for word_ws, word_pos in zip(sentence_ws, sentence_pos):
        res.append(f"{word_ws}({word_pos})")
    return "\u3000".join(res)


if __name__ == "__main__":
    main()