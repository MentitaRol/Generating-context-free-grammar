import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> VSO | SVO
    VSO -> V NP NP | V Sub Sub
    SVO -> NP V NP | Sub V Sub
    V -> VTran | VIntran
    
    NP -> NPA | NPAd | NS
    
    NPA -> Sub Adpo | Adpo Sub 
    NPAd -> Adj Sub | Sub Adj
    NS -> Adj Sub Adpo | Adpo Sub Adj | Adj Adpo Sub
    
    Sub -> NCase | ProNCase
    NCase -> NAgen | NPatien
    ProNCase -> ProNAgen | ProNPatien

    VTran -> 'kllkem' | 'eykefu' | 'si' | 'taron' | 'tìreysi' | 'sngä' | 'kame' | 'nume'
    VIntran -> 'tìran' | 'tswayon' | 'srew' | 'yom' | 'zup' | 'kim' 
    NAgen -> 'oel' | 'pol' | 'tutel' | 'tsamsiyuìl' | 'ikranìl'
    NPatien -> 'payoangit' | 'tutet' | 'yerikit' | 'pukit' | 'ikranti'
    ProNAgen -> 'ayoel' | 'ngal' | 'ayfol' | 'mefol' | 'ayngal'
    ProNPatien -> 'oeti' | 'mefoti' | 'oengati' | 'ayoengati' | 'poti' | 'ngati'
    Adpo -> 'mì' | 'hu' | 'sì' | 'ro' | 'ta' | 'na' | 'äo' | 'eo'
    Adj -> 'ngim' | 'lefpom' | 'tsawl' | 'sìltsan' | 'txur' | 'hìi'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentences = [
    # Correct sentences
    "pol eykefu oeti",
    "tsamsiyuìl taron yerikit",
    "tutel kame pukit",
    "oel kame ngati",
    "kllkem oel pol",
    "tìreysi mefol tsamsiyuìl",
    "tutel txur tswayon hu ikranti",
    "kame ngati lefpom eo yerikit hìi",
    "mì ayfol sìltsan tìreysi tsamsiyuìl txur",
    "ayoel ro srew lefpom sì oel",
    "zup ikranti ta oel tsawl",
    "yom pol sìltsan tsawl payoangit",
    "kllkem ikranìl txur tutet sìltsan",
    "kame oel mì tutet ngim",
    "pukit sìltsan nume mì oel",
    "kllkem tsamsiyuìl txur tutet hìi",
    "tìreysi ayoel ro tutet sìltsan",
    "nume ngal ta pukit ngim",
    "mì ikranìl tsawl tswayon ayfol sìltsan",
    
    # Incorrect sentences
    "tsamsiyuìl txur taron yerikit hu tsamsiyuìl lefpom",
    "txur ikranìl ro ngim yerikit eykefu poti",
    "oel sì ayoel lefpom srew ro",
    "tsamsiyuìl tìran ro ngim",
    "ayoel si mì tsawl mefoti",
    "mefol taron ta yerikit"
]

for sentence in sentences:
    # Tokenize the sentence
    tokens = sentence.split()
    # Parse the sentence and convert it to a list
    trees = list(parser.parse(tokens))
    
    if trees:
        print(f"The tree for the sentence \"{sentence}\" is:")
        for tree in trees:
            tree.pretty_print()
            print()
    else:
        print(f"The sentence \"{sentence}\" is not part of the language")