Data Used:
The CiteSeer UMD collection is a standard text document collection, consisting of abstracts of
research articles from Computer Science, which are sampled from the CiteSeer digital library.

---Functionality- 


First, all the dataset files are parsed. Then preprocessing of the text in those files takes place.

Various preprocessing steps in this program are:

	1.Punctuation removal
	Here, we strip all punctuation from the text using string.punctuation from the string library.


	2.Tokenization
	The text of the document is first converted into lowercase and then been split using whitespaces.

	3.Stopword Removal
	All stopwords from the nltk.corpus have been removed from the tokenized words.

	4.Stemming
	Porter Stemmer from the nltk library is used for stemming.

First, we try only punctuation removal and tokenization and find out the following:
	1. The total number of words in the collection
	2. Vocabulary size
	3. Top 20 frequent words
	4. Stop words occurring in those top 20 frequent words
	5. The minimum number of unique words accounting for 15% of the total number of words in the collection

Then we use stopword removal and stemming along with punctuation removal and tokenization and find out the same 5 values again.


---Answers to the questions asked:

Total number of words in the collection:  476198
Vocabulary size:  19886

Top 20 words with highest frequencies are:
('the', 25662)
('of', 18638)
('and', 14131)
('a', 13345)
('to', 11536)
('in', 10067)
('for', 7379)
('is', 6577)
('we', 5138)
('that', 4820)
('this', 4446)
('are', 3737)
('on', 3656)
('an', 3281)
('with', 3200)
('as', 3057)
('by', 2765)
('data', 2691)
('be', 2500)
('information', 2322)

From these top 20 words, the stop words are:
('the', 25662)
('of', 18638)
('and', 14131)
('a', 13345)
('to', 11536)
('in', 10067)
('for', 7379)
('is', 6577)
('we', 5138)
('that', 4820)
('this', 4446)
('are', 3737)
('on', 3656)
('an', 3281)
('with', 3200)
('as', 3057)
('by', 2765)
('be', 2500)
Number of stop words in top 20 words:  18
Minimum number of unique words accounting for 15% of the total number of words in the collection:  4

After Stemming and stop words removal

Total number of words in the collection after stemming and stop words removal are:  294256
Vocabulary size after stemming and stop words removal:  13778

Top 20 words with highest frequencies after stemming and stop words removal:
('system', 3741)
('use', 3740)
('data', 2691)
('agent', 2688)
('inform', 2398)
('model', 2315)
('paper', 2246)
('queri', 1905)
('user', 1756)
('learn', 1740)
('algorithm', 1584)
('1', 1552)
('approach', 1544)
('problem', 1543)
('applic', 1522)
('present', 1507)
('base', 1486)
('web', 1439)
('databas', 1424)
('comput', 1411)

From these top 20 words, the stop words are:
Number of stop words in top 20 words:  0
Minimum number of unique words accounting for 15% of the total number of words in the collection:  24

