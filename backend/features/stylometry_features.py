import spacy
import textstat

nlp = spacy.load("en_core_web_sm")


def get_function_word_ratio(doc):
    """% of words that are function words (determiners, prepositions, conjunctions, pronouns, auxiliary verbs)"""
    function_pos_tags = {"DET", "ADP", "CCONJ", "SCONJ", "PRON", "AUX"}
    words = [token for token in doc if token.is_alpha]
    if not words:
        return 0
    function_words = [token for token in words if token.pos_ in function_pos_tags]
    return round(len(function_words) / len(words) * 100, 2)


def extract_stylometry_features(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    words = [token for token in doc if token.is_alpha]

    avg_sentence_length = round(len(words) / len(sentences), 2) if sentences else 0
    avg_word_length = round(sum(len(token.text) for token in words) / len(words), 2) if words else 0
    flesch_score = round(textstat.flesch_reading_ease(text), 2)
    function_word_pct = get_function_word_ratio(doc)

    return {
        "Avg Sentence Length (words)": avg_sentence_length,
        "Avg Word Length (chars)": avg_word_length,
        "Flesch Reading Ease": flesch_score,
        "Function Word %": function_word_pct
    }


if __name__ == "__main__":
    sample_text = """All the patterns I've seen in highly ambitious people, of the ways in which they keep themselves busy; to get a sense of work but at the same time make no actual progress towards their goals; are ways to avoid it. Focusing on redundant work with little to no meaning, hyper-fixating on perfectionism, over/under scheduling; to name a few. I cannot be aware of everybody's experiences but on an anecdotal basis, I think it is because when people who've had a background of no tangible successes get a taste of it-a sense of its glory, one of two things happens. They either take themselves to be fraudulent because they've internalised the feeling of never being able to achieve anything. Or, because an insignificant past in terms of one's achievements usually involves the lack of a system, they're unable to sustain/maintain the glory, and now it actually seems like an accident/fraud."""
    result = extract_stylometry_features(sample_text)
    print(result)