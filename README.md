# Generating and cleaning a restricted context free grammar
In this second evidence we analyze the Na’vi language and construct a context-free grammar (CFG) to formally determine whether given sentences belong to the language.

## Description
Na’vi is a constructed language created by Dr. Paul Frommer for Avatar, the 2009 film directed by James Cameron. The language has been growing and expanding due to continuous work by eager fans and the language creator. (Kelutral, n. d.)

Na’vi features a rich phonetic system and a verb-subject-object (VSO) syntax, making it an excellent candidate for formal linguistic analysis through context-free grammars.

### Na’vi Language Characteristics

#### Word order and Syntax
Na’vi language follows a Verb-Subject-Object (VSO) word order. This means that in a typical sentence the verb comes first, followed by the subject and then the object.

For example: 

Lom tute ikran – Sees person banshee → “The person sees the banshee”

The order of Subject, Object and Verb is not constrained, allowing six core structures based on speaker preference.

For example, for the sentence ‘I eat Fish’ we can express it like:

1.	oel payoangti yom
2.	payoangti yom oel
3.	yom oel payoangti
4.	oel yom payoangti
5.	payoangti oel yom
6.	yom payoangti oel

(Kelutral, n. d.)

#### Adjectives and Morphology
Adjectives can precede or follow nouns. 

When preceding, the adjective takes a suffix … a.
When following, it takes a prefix a … 

For example, "ngima kilvan" and "kilvan angim" both mean "long river."

#### Noun Cases
Na'vi has what is referred to as "limited free word order", which means that in most circumstances the way a sentence is arranged is subject to how the speaker wants it to flow. This is achieved through marking nouns for their role in a sentence via noun case endings, which helps to identify their role in the sentence regardless of placement. (Kelutral, n. d.).

Na'vi nouns have 5 noun cases: agentive, patientive, genitive, dative, and topical.

Case endings
•	Agentive -l or -ìl, used for the subject of a transitive verb 
•	Patientive -t, -it, or -ti, used for the direct object of a transitive verb 
•	Genitive -ä or -yä, used to create possessive nouns 
•	Dative -r(u) or -ur, used for indirect objects 
•	Topical -ìri or -ri, used to set context for a sentence or to make a direct object into an intransitive verb 

#### Adpositions
Adpositions in Na’vi often function similarly to prepositions in English. They can either precede a noun or appear as suffixes, modifying the noun much like adjectives.

They cannot be used independently of nouns. Some adpositions can cause lenition (Kelutral, n. d.).

### Scope and Limitations
Due to the complexity of the Na'vi language, this project will focus on a simplified subset that is sufficiently expressive to allow the construction of complete sentences.

The following outlines the specific elements of the language that will be included in this analysis:

#### Syntax
Na’vi typically follows a Verb-Subject-Object (VSO) word order, but the language syntax is highly flexible, allowing for up to six different word orders.

For the purposes of this project, only two structures will be considered:
•	VSO (Verb-Subject-Object), the most frequently used word order in Na’vi.
•	SVO (Subject-Verb-Object), which is more common in languages like English.

#### Prefixes, Infixes, and Suffixes
Na’vi is an agglutinative language. This means that prefixes, infixes, and suffixes are attached to root words to convey grammatical relationships and meanings (such as tense, number, case, etc.) (Kelutral, n. d.).

To simplify the grammar and keep it within the capabilities of a context-free model:

• Only case suffixes will be included, as they are essential to identifying the grammatical role of a noun in a sentence.
• Prefixes and infixes will be excluded from this model due to their complexity. In particular, infixes, are difficult to represent using context-free grammar.
• As a result, verbs will appear in their base form, without any inflection for tense, aspect, mood, or other grammatical categories. 
• Pronouns will be treated as separate words rather than verb affixes.

#### Noun Cases
Na'vi includes five grammatical cases: agentive, patientive, genitive, dative, and topical. For this project, we will focus on two:

•	Agentive
•	Patientive

These two cases are sufficient to distinguish between transitive and intransitive verb structures and will provide a manageable level of complexity.

#### Adpositions
Some adpositions trigger lenition, a phonetic phenomenon that alters the initial sound of the following word.

Because lenition is a phonological rule and cannot be captured by context-free grammar, it will not be modeled in this project. We will only use the most frequent and structurally consistent adpositions.

## Models
To determine whether a sentence belongs to the Na'vi language, we will follow the principles of syntax analysis, also known as parsing.

Syntax analysis is the second phase in the process of compiler design, following lexical analysis. Its primary objective is to verify the syntactic structure of a given input based on the formal grammar of the language. This is achieved by constructing a data structure known as a parse tree or syntax tree, which represents the hierarchical syntactic structure of the input. (GeeksforGeeks, 2025)

The parser uses the predefined grammar rules of the language to build this tree. If the input string can be derived from the grammar and successfully mapped to the parse tree, it is considered syntactically correct. Otherwise, the parser will report a syntax error. (GeeksforGeeks, 2025)

There are many types of parsers, the main difference is the order in which they read and how they build the parse tree or abstract syntax tree (AST).

For this project, we will implement an LL(1) parser, which is one of the simplest and most commonly used types of parsers. It uses a predictive, top-down approach. This allows for efficient parsing without backtracking. (GeeksforGeeks, 2025)

To successfully implement an LL(1) parser, we must ensure that the grammar used satisfies the requirements of LL(1) parsing. These include:

•	Defining a grammar that accurately recognizes the structure of the Na'vi language.
•	Eliminating any ambiguity within the grammar.
•	Removing left recursion, which is not allowed in LL(1) grammars.

### 1.- Generate a grammar that recognizes the language.
The following context-free grammar was developed to simulate an abstraction of the Na'vi language. 

    S -> VSO | SVO
    VSO -> V NP NP
    SVO -> NP V NP
    V -> VTran | VIntran
    NP ->  Sub | Sub Adpo | Adpo Sub | Adj Sub | Sub Adj | Adj Sub Adpo | Adpo Sub Adj | Adj Adpo Sub
    NP -> NP NP
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

#### Key Features of the Grammar:
**Syntactic Flexibility:** The grammar supports both major sentence structures found in Na'vi:
•	VSO (Verb-Subject-Object)
•	SVO (Subject-Verb-Object)

**Verb Types:** It distinguishes between transitive and intransitive verbs through the rule V -> VTran | VIntran.

**Noun Phrase Construction (NP):** Noun phrases support multiple variations, allowing flexibility in the order of:
•	Adpositions (prepositions/postpositions)
•	Adjectives
•	Nouns or Pronouns

Noun phrases can also be recursively combined (NP -> NP NP) to allow more complex expressions.

**Noun Cases:** The grammar includes the two most common noun cases in Na'vi:
•	Agentive (NAgen, ProNAgen): indicates the doer of an action
•	Patientive (NPatien, ProNPatien): indicates the receiver of an action

### 2.- Eliminate Ambiguity in the grammar.
Now that we have defined the first version of our grammar, the next step is to ensure that it is free of ambiguity.

A grammar is considered ambiguous if a single sentence can be derived in more than one way, resulting in multiple parse trees. This means that the sentence can be interpreted in different ways depending on how it is parsed, which is problematic for building a reliable syntax analyzer. (GeeksforGeeks, 2025)

Analyzing our grammar, we realize that the main source of ambiguity lies in the rules:

    NP -> Sub | Sub Adpo | Adpo Sub | Adj Sub | Sub Adj | Adj Sub Adpo | Adpo Sub Adj | Adj Adpo Sub
    NP -> NP NP

The first set of rules introduces ambiguity due to the flexible ordering of elements within a noun phrase (NP). The second rule (NP -> NP NP) allows for recursive in noun phrases, which also leads to multiple valid derivations for the same input.

To resolve this, we need to restructure them into more specific and modular components:

We define three subcategories of noun phrases:
•	**NPA:** Noun phrases with adpositions
    NPA -> Sub Adpo | Adpo Sub
•	**NPAd:** Noun phrases with adjectives
    NPAd -> Adj Sub | Sub Adj
•	**NS:** Extended noun phrases with both adjectives and adpositions
    NS -> Adj Sub Adpo | Adpo Sub Adj | Adj Adpo Sub

Additionally, we are going to include new rules in the VSO and SVO structures to allow the creation of simple sentences with only subjects without these having to be necessarily linked to adjectives or adpositions. This also eliminate the ambiguity generated in the NP rule that allows multiple subjects to be added to sentences. 

•	VSO -> V NP NP | V Sub Sub
•	SVO -> NP V NP | Sub V Sub

So, the NP rule has finally been transformed into:
    NP -> NPA | NPAd | NS

    NPA -> Sub Adpo | Adpo Sub
    NPAd -> Adj Sub | Sub Adj
    NS -> Adj Sub Adpo | Adpo Sub Adj | Adj Adpo Sub

To see how this works more clearly, let's try an example with our first grammar generated in step 1: "Generate a grammar that recognizes the language."

We'll try the sentence: "taron oel ngim äo tutet"

With the first grammar model, this sentence generates ambiguity because it can be derived in multiple ways.
![Image](https://github.com/user-attachments/assets/5f65da0b-fb76-4ffb-90fa-eee337ce03ba)

![Image](https://github.com/user-attachments/assets/5cb2f3cf-1e7b-4776-b1c1-667da01175f2)

This ambiguity occurs because the NP rule encompasses all possible combinations of a sentence, making it difficult to clearly identify which elements belong to each noun phrase and what syntactic roles they play.

With the second model, the ambiguity is eliminated because specific rules are established for each type of noun phrase.

![Image](https://github.com/user-attachments/assets/c57cac77-de6f-4333-8d81-5bdd60ef388d)

In the second grammar, noun phrases are categorized into specific types (NPA, NPAd, NS), eliminating the ambiguity of the NP rule.

### 3.- Eliminate left recursion in the grammar.
With the disambiguation of our grammar complete, we can now proceed to analyze it for left recursion, which is another common issue that must be addressed in LL(1) parsers.

According to Scaler:

>"In compiler design, left recursion occurs when a grammar rule refers to itself in a way that hampers parsing." (Scaler, 2024)

So we can see that Left recursion is present in a grammar when a non-terminal symbol recursively calls itself as the first symbol in one of its production rules. 
A typical pattern for direct left recursion is:
    A -> A a | B

Where the nonterminal A references itself on the left side, resulting in an infinite loop.

After checking all production rules in our updated grammar, we found that no left recursion is present. This is primarily due to the structural changes made during the disambiguation process, particularly in the elimination of recursive constructs like NP → NP NP.
As a result, our grammar is free of left recursion and is structurally compatible with the requirements of LL(1) parsing.

## Implementation
To implement and test our models, we will be working with the nltk (Natural Language Toolkit) Python library, which is a very powerful tool that allows us to perform various tasks such as tokenization, morpho-syntactical labeling, sentiment analysis, etc.

It's important that if you don't have nltk installed before you install it correctly. Here’s how to install it:

1.- Open your terminal or command prompt.

2.- Run the following command:

    pip install nltk

Once nltk is installed we import the nltk library from Python and the CFG module from nltk to use Context free grammar

    import nltk
    from nltk import CFG

To split the sentences into tokens, we use nltk.download('punkt'). This downloads the tokenizer model required for breaking down text into individual words.

    nltk.download('punkt')

Then we define our context-free grammar

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

With the grammar defined, we create a parser that will use this grammar to parse input sentences and generate syntax trees.

    parser = nltk.ChartParser(grammar)

To correctly test our grammar, we define a set of correct and incorrect sentences (we will go into more detail on this in the testing stage)

    sentences = [
        # Correct sentences
        "pol eykefu oeti",
        "tsamsiyuìl taron yerikit",
        "tutel kame pukit",
        "oel kame ngati",
        ...
    ]

The sentences are processed in a loop where each sentence is split into tokens using the .split() function.

    for sentence in sentences:
        tokens = sentence.split()

The sentence tokens are passed to the parser, which tries to match the grammar and generate possible syntax trees.

    trees = list(parser.parse(tokens))

If valid syntax trees are found, we printed using tree.pretty_print(). If no trees are found, a message is printed indicating that the sentence does not belong to the language.

    if trees:
        print(f"The tree for the sentence \"{sentence}\" is:")
        for tree in trees:
            tree.pretty_print()
            print()
    else:
        print(f"The sentence \"{sentence}\" is not part of the language")

## References
Learn Na’vi. (2011). Grammar. https://learnnavi.org/navi-grammar/

Kelutral. (n. d). Learn the Na’vi Language Online at Kelutral.org. https://kelutral.org/ 

Kelutral. (n. d). Na’vi linguistic information. https://kelutral.org/linguistics