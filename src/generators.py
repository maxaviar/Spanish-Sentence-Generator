from utils import load_json
import random

## skeleton 1: [subject] + ir + a + [verb] + [place]
def GenerateIr() -> str:
    ## load data
    nouns_list = load_json("nouns.json")
    places_list = load_json("places.json")
    subject_list = load_json("subject.json")
    times_list = load_json("times.json")
    verbs_dict = load_json("verbs.json")

    ## choose a random subject
    subject_idx = random.randrange(len(subject_list))

    ## choose the correct conjugation and add "ir" + "a" to str
    sentence_ir = verbs_dict["ir"]["present"][subject_idx]
    sentence = f"{sentence_ir} a"

    ## choose the correct conjugation and add "verb" + "place"
    verb_key = random.choice(list(verbs_dict.keys()))
    sentence += f" {verb_key} {random.choice(places_list)["es"]}"

    ## return string
    return sentence