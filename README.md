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


## References
Learn Na’vi. (2011). Grammar. https://learnnavi.org/navi-grammar/

Kelutral. (n. d). Learn the Na’vi Language Online at Kelutral.org. https://kelutral.org/ 

Kelutral. (n. d). Na’vi linguistic information. https://kelutral.org/linguistics