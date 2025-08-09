
from django.shortcuts import render
from nltk.corpus import wordnet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search= request.GET.get('search')

    meaning =[] 
    synonyms = set()
    antonyms =set()

    if search:
        synsets=wordnet.synsets(search)

        if synsets:
            for syn in synsets[:3]:
                meaning.append(syn.definition())
                
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name())

                    if lemma.antonyms():
                        antonyms.add(lemma.antonyms()[0].name())
    else:
        meaning.append('no definition found.')
    context = {
        'meaning': (meaning),
        'synonyms':list(synonyms),
        'antonyms': list(antonyms),
        'word': search,
    }
    return render(request, 'word.html', context)
