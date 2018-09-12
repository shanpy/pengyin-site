.. title: Search Engine Basics (Including Lucene)
.. date: 2015-07-21
.. category: Data Science
.. tags: Data Science, Hydra, Search Engine, SEO
.. slug: search-engine-basics-lucene
.. authors: Pengyin Shan
.. description: This posts will be continously updated, including intersting serach engine knowledge I found online, with introduction to Lucene

##Reference List

- <a href="http://www.tutorialspoint.com/lucene/lucene_overview.htm">Lucene Tutorial from TutorialPoint.com</a>

##Search Engine Basics

###Search Application Operation List

1. **Acquire Raw Content**: Collect the target contents on which search are to be conducted.

2. **Build the document**:  Build the document(s) from the raw contents which search application can understands and interpret easily.

3. **Analyze the document**: The document is to be analyzed as which part of the text is a candidate to be indexed.

4. **Indexing the document**: Index documents so that this document can be retrived based on certain keys instead of whole contents of the document.

5. **User Interface for Search**: To facilitate user to make a search, application must provide a user a mean or u0ser interface where a user can enter text and start the search process.

6. **Build Query**: Once user made a request to search a text, application should prepare a Query object using that text which can be used to inquire index database to get the relevant details.

7. **Search Query**: Using query object, index database is then checked to get the relevant details and the content documents.

8. **Render Results**: Once result is received the application should decide how to show the results to the user using User Interface. How much information is to be shown at first look and so on.

##Lucene Basics

###Setup

Lucene performs step 2 to step 7 in `Search Application Operation List` section above.

You need `JDK` for Lucene setup. You can view setup process <a href="http://www.tutorialspoint.com/lucene/lucene_environment.htm">here</a>.

###Index Process

In Lucene, `IndexWriter` is the most important and core component of the indexing process.

Process Chart for TutorialsPoint:

images/articles/2015/data/indexing_process.jpg 

>We add Document(s) containing Field(s) to IndexWriter which analyzes the Document(s) using the Analyzer and then creates/open/edit indexes as required and store/update them in a Directory. IndexWriter is used to *update or create* indexes. It is not used to read indexes.

####List of Indexing Classes

1. <a href="http://www.tutorialspoint.com/lucene/lucene_indexwriter.htm">IndexWriter</a>: This class acts as a core component which **creates/updates indexes** during indexing process.

2. <a href="http://www.tutorialspoint.com/lucene/lucene_directory.htm">Directory</a>: This class represents the **storage** location of the indexes.

3. <a href="http://www.tutorialspoint.com/lucene/lucene_analyzer.htm">Analyzer</a>: Analyzer class is responsible to **analyze** a document and **get the tokens/words from the text** which is to be indexed. Without analysis done, IndexWriter can not create index.

4. <a href="http://www.tutorialspoint.com/lucene/lucene_document.htm">Document</a>: Document represents a **virtual document** with Fields where Field is object which can contain the physical document's contents, its meta data and so on. Analyzer can understand a Document only.

5. <a href="http://www.tutorialspoint.com/lucene/lucene_field.htm">Field</a>: Field is the **lowest unit or the starting point** of the indexing process. It represents the `key-value` pair relationship where a key is used to identify the value to be indexed. Say a field used to represent contents of a document will have key as "contents" and the value may contain the part or all of the text or numeric content of the document. Lucene can index only **text or numeric** contents only.

####List of Search Classes

Searching process is again one of the core functionality provided by Lucene.

It's flow is similar to that of indexing process. Basic search of lucene can be made using following classes which can also be termed as foundation classes for all search related operations:

1. <a href="http://www.tutorialspoint.com/lucene/lucene_indexsearcher.htm">IndexSearcher</a>: This class act as a core component which **reads/searches indexes** created after indexing process. It takes directory instance pointing to the location containing the indexes.

2. <a href="http://www.tutorialspoint.com/lucene/lucene_term.htm">Term</a>: This class is the **lowest** unit of searching. It is similar to Field in indexing process.

3. <a href="http://www.tutorialspoint.com/lucene/lucene_query.htm">Query</a>: Query is an abstract class and contains various utility methods and is the parent of all types of queries that lucene uses during search process.

4. <a href="http://www.tutorialspoint.com/lucene/lucene_termquery.htm">TermQuery</a>: TermQuery is the **most commonly used query object** and is the foundation of many complex queries that lucene can make use of.

5. <a href="http://www.tutorialspoint.com/lucene/lucene_topdocs.htm">TopDocs</a> : TopDocs points to the top N search results which matches the search criteria. It is simple container of pointers to point to documents which are output of search result.

####Create a Document

1. Create a method to **get a lucene document** from a text file.

2. Create various types of fields which are `key-value` pairs containing keys as **names** and **values** as contents to be indexed.

3. Set field to be analyzed or not. In our case, only contents is to be analyzed as it can contain data such as `a`, `am`, `are`, `an` etc. which are not required in search operations.

Example Code from TutorialsPoint:

    :::java
    private Document getDocument(File file) throws IOException{
        Document document = new Document();
        //index file contents
        Field contentField = new Field(LuceneConstants.CONTENTS, new FileReader(file));
        //index file name
        Field fileNameField = new Field(LuceneConstants.FILE_NAME, file.getName(), Field.Store.YES, Field.Index.NOT_ANALYZED);
        //index file path
        Field filePathField = new Field(LuceneConstants.FILE_PATH, file.getCanonicalPath(), Field.Store.YES,Field.Index.NOT_ANALYZED);
        document.add(contentField);
        document.add(fileNameField);
        document.add(filePathField);
        return document;
    }

####Create a IndexWriter

1. IndexWriter class acts as a core component which **creates/updates** indexes during indexing process.

2. Create object of `IndexWriter`.

3. Create a `lucene directory` which should point to location where indexes are to be stored.

4. Initialize the IndexWriter object created with the index directory, a standard analyzer having version information and other required/optional parameters.

Example Code from TutorialsPoint:

    :::java
    private IndexWriter writer;
    public Indexer(String indexDirectoryPath) throws IOException{
       //this directory will contain the indexes
       Directory indexDirectory = FSDirectory.open(new File(indexDirectoryPath));
       //create the indexer
       writer = new IndexWriter(indexDirectory, new StandardAnalyzer(Version.LUCENE_36),true, IndexWriter.MaxFieldLength.UNLIMITED);
    }

####Start Indexing Process

    :::java
    private void indexFile(File file) throws IOException{
       System.out.println("Indexing "+file.getCanonicalPath());
       Document document = getDocument(file);
       writer.addDocument(document);
    }

###Basic Indexing Operations

####Add Document Operation

Add document is one of the core operation as part of indexing process.

1. **Add a document to an index**: Refer to `Create a Document` section above for process. After last step, add the newly created fields to the document object and return it to the caller method.

2. **Create a IndexWriter**: Refer to `Create a IndexWriter` section above for process.

3. **Add document and start Indexing process**: Two ways.

>Way 1: **addDocument(Document)** - Adds the document using the default analyzer (specified when index writer is created.)

>Way 2: **addDocument(Document,Analyzer)** - Adds the document using the provided analyzer.

Refer "Start Indexing Process" section above for code reference.

####Update Document Operation

Update document is another important operation as part of indexing process.

This operation is used when already indexed contents are updated and indexes become invalid. This operation is also known as `re-indexing`.

We update Document(s) containing Field(s) to `IndexWriter` where `IndexWriter` is used to update indexes.

1. **Update a document to an index**: Create a method to update a lucene document from an updated text file.

>
    :::java
    private void updateDocument(File file) throws IOException{
       Document document = new Document();

       //update indexes for file contents
       writer.updateDocument(new Term
          (LuceneConstants.CONTENTS,
          new FileReader(file)),document);
       writer.close();
    }

2. **Create a IndexWriter**: Same as above.

3. **Update document and start reindexing process**: Two Ways.

>Way1: **updateDocument(Term, Document)**: *Delete* the document containing the term and *add* the document using the default analyzer (specified when index writer is created.)

>Way2: **updateDocument(Term, Document,Analyzer)**: *Delete* the document containing the term and *add* the document using the provided analyzer.

>
    :::java
    private void indexFile(File file) throws IOException{
       System.out.println("Updating index for "+file.getCanonicalPath());
       updateDocument(file);
    }

####Delete Document Operation

Delete document is another important operation as part of indexing process.

This operation is used when already indexed contents are updated and indexes become invalid or indexes become very large in size then *in order to reduce the size and update the index*, delete operations are carried out.

We delete Document(s) containing Field(s) to `IndexWriter` where `IndexWriter` is used to update indexes.

1. **Delete a document from an index** : Create a method to delete a lucene document of an obsolete text file.

>
    :::java
    private void deleteDocument(File file) throws IOException{
       //delete indexes for a file
       writer.deleteDocument(new Term(LuceneConstants.FILE_NAME,file.getName()));
       writer.commit();
       System.out.println("index contains deleted files: "+writer.hasDeletions());
       System.out.println("index contains documents: "+writer.maxDoc());
       System.out.println("index contains deleted documents: "+writer.numDoc());
    }

2. **Create a IndexWriter**: Same as above

3. **Delete document and start reindexing process**: Five ways.

>Way1: **deleteDocuments(Term)**: Delete all the documents containing the term.

>Way2: **deleteDocuments(Term[])**: Delete all the documents containing any of the terms in the array.

>Way3: **deleteDocuments(Query)**: Delete all the documents matching the query.

>Way4: **deleteDocuments(Query[])**: Delete all the documents matching the query in the array.

>Way5: **deleteAll**: Delete all the documents.

    :::java
    private void indexFile(File file) throws IOException{
       System.out.println("Deleting index for "+file.getCanonicalPath());
       deleteDocument(file);
    }

####Field Options

Field is the most important and the foundation unit of indexing process.

It is the actual object containing the contents to be indexed. When we add a field, lucene provides numerous controls on the field using Field Options which states how much a field is to be searchable.

We add Document(s) containing Field(s) to `IndexWriter` where `IndexWriter` is used to update or create indexes.

#####List of Field Options

- `Index.ANALYZED`: First analyze then do indexing. Used for *normal text indexing*. Analyzer will break the field's value into stream of tokens and each token is searcable sepearately.

- `Index.NOT_ANALYZED`: Don't analyze but do indexing. Used for *complete text indexing* *for example person's names, URL etc.

- `Index.ANALYZED_NO_NORMS`: Varient of `Index.ANALYZED`. Analyzer will *break the field's value into stream of tokens* and each token is searcable sepearately but `NORMs` are not stored in the indexes. `NORMS` are used to boost searching but are sometime memory consuming.

- `Index.Index.NOT_ANALYZED_NO_NORMS`:  Varient of `Index.NOT_ANALYZED`. Indexing is done but NORMS are not stored in the indexes.

- `Index.NO`: Field value is not searchable.

#####Use of Field Options

1. Same steps as `Create a Document` section

2. Add the newly created fields to the document object and return it to the caller method.

###Search Operations

Searching process is one of the core functionality provided by Lucene.

`IndexSearcher` is the most important and core component of the searching process.

Process Chart for TutorialsPoint:

images/articles/2015/data/searching_process.jpg 

We first create `Directory`(s) containing `index`es and then pass it to `IndexSearcher` which opens the `Directory` using `IndexReader`.

Then we create a `Query` with a `Term` and make a search using `IndexSearcher` by passing the `Query` to the searcher.

`IndexSearcher` returns a `TopDocs` object which contains the search details along with document `ID`(s) of the Document which is the result of the search operation.

####Create a QueryParser

1. QueryParser class parses the user entered input into **lucene understandable format query**.

2. Create object of `QueryParser`.

3. Initialize the QueryParser object created with a standard analyzer having version information and index name on which this query is to run.

>
    :::java
    QueryParser queryParser;
    public Searcher(String indexDirectoryPath) throws IOException{
       queryParser = new QueryParser(Version.LUCENE_36,
          LuceneConstants.CONTENTS,
             new StandardAnalyzer(Version.LUCENE_36));
    }

####Create a IndexSearch

1. `IndexSearcher` class acts as a core component which searcher indexes created during indexing process.

2. Create object of `IndexSearcher`.

3. Create a **lucene directory** which should point to location where indexes are to be stored.

4. Initialize the `IndexSearcher` object created with the index directory

>
    :::java
    IndexSearcher indexSearcher;
    public Searcher(String indexDirectoryPath) throws IOException{
       Directory indexDirectory =
          FSDirectory.open(new File(indexDirectoryPath));
       indexSearcher = new IndexSearcher(indexDirectory);
    }

####Make search

- To start search, create a `Query` object by parsing search expression through QueryParser.

- Make search by calling `IndexSearcher.search()`` method.

>
    :::java
    Query query;
    public TopDocs search( String searchQuery) throws IOException,ParseException{
       query = queryParser.parse(searchQuery);
       return indexSearcher.search(query, LuceneConstants.MAX_SEARCH);
    }

####Get the document

    :::java
    public Document getDocument(ScoreDoc scoreDoc)
       throws CorruptIndexException, IOException{
       return indexSearcher.doc(scoreDoc.doc);
    }

####Close IndexSearcher

    :::java
    public void close() throws IOException{
       indexSearcher.close();
    }

###Query Programming

<a href="http://www.tutorialspoint.com/lucene/lucene_termquery1.htm">TermQuery</a>: TermQuery is the most commonly used query object and is the foundation of many complex queries that lucene can make use of. TermQuery is normally used to retrieve documents based on the key which is case sensitive.

<a href="http://www.tutorialspoint.com/lucene/lucene_termrangequery.htm">TermRangeQuery</a>: TermRangeQuery is the used when a range of textual terms are to be searched.

<a href="http://www.tutorialspoint.com/lucene/lucene_prefixquery.htm">PrefixQuery</a>: PrefixQuery is used to match documents whose *index starts with a specified string*.

<a href="http://www.tutorialspoint.com/lucene/lucene_booleanquery.htm">BooleanQuery</a>: BooleanQuery is used to search documents which are result of multiple queries using `AND`, `OR` or `NOT` operators.

<a href="http://www.tutorialspoint.com/lucene/lucene_phrasequery.htm">PhraseQuery</a>: Phrase query is used to search documents which contain a particular sequence of terms.

WhildCardQuery: WildcardQuery is used to search documents using wildcards like `*` for any character sequence,`?` matching a single character.

<a href="http://www.tutorialspoint.com/lucene/lucene_fuzzyquery.htm">FuzzyQuery</a>: FuzzyQuery is used to search documents using **fuzzy implementation** that is an approximate search based on edit distance algorithm.

<a href="http://www.tutorialspoint.com/lucene/lucene_matchalldocsquery.htm">MatchAllDocsQuery</a>: MatchAllDocsQuery as name suggests *matches all the documents*.

###Analysis Objects

<a href="http://www.tutorialspoint.com/lucene/lucene_token.htm">Token</a>: Token represents text or word in a document with relevant details like its **metadata** (position, start offset, end offset, token type and its position increment).

<a href="http://www.tutorialspoint.com/lucene/lucene_tokenstream.htm">TokenStream</a>: TokenStream is an output of analysis process and it comprises of series of tokens. It is an abstract class.

<a href="http://www.tutorialspoint.com/lucene/lucene_analyzer_class.htm">Analyzer</a>: Analyzer class is responsible to analyze a document and get the tokens/words from the text which is to be indexed. Without analysis done, IndexWriter can not create index.

<a href="http://www.tutorialspoint.com/lucene/lucene_whitespaceanalyzer.htm">WhitespaceAnalyzer</a>: This analyzer spilts the text in a document based on **whitespace**.

<a href="http://www.tutorialspoint.com/lucene/lucene_simpleanalyzer.htm">SimpleAnalyzer</a>: This analyzer spilts the text in a document based on **non-letter characters** and then lowercase them.

<a href="http://www.tutorialspoint.com/lucene/lucene_stopanalyzer.htm">StopAnalyzer</a>: This analyzer works similar to SimpleAnalyzer and remove the common words like `a`,`an`,`the` etc.

<a href="http://www.tutorialspoint.com/lucene/lucene_standardanalyzer.htm">StandardAnalyzer</a>: This is the most sofisticated analyzer and is capable of handling `names`, `email address` etc. It lowercases each token and removes common words and punctuation if any.

###Sorting

####Sorting By Relevance

This is **default** sorting mode used by lucene.

Lucene provides results by the most relevant hit at the top.

Example Code from TutorialsPoint:

    :::java
    private void sortUsingRelevance(String searchQuery)
     throws IOException, ParseException{
       searcher = new Searcher(indexDir);
       long startTime = System.currentTimeMillis();
       //create a term to search file name
       Term term = new Term(LuceneConstants.FILE_NAME, searchQuery);
       //create the term query object
       Query query = new FuzzyQuery(term);
       searcher.setDefaultFieldSortScoring(true, false);
       //do the search
       TopDocs hits = searcher.search(query,Sort.RELEVANCE);
       long endTime = System.currentTimeMillis();
       System.out.println(hits.totalHits +
          " documents found. Time :" + (endTime - startTime) + "ms");
       for(ScoreDoc scoreDoc : hits.scoreDocs) {
          Document doc = searcher.getDocument(scoreDoc);
          System.out.print("Score: "+ scoreDoc.score + " ");
          System.out.println("File: "+ doc.get(LuceneConstants.FILE_PATH));
       }
       searcher.close();
    }

####Sorting By IndexOrder

This is sorting mode used by lucene in which first document indexed is shown first in the search results.

    :::java
    private void sortUsingIndex(String searchQuery)
     throws IOException, ParseException{
       searcher = new Searcher(indexDir);
       long startTime = System.currentTimeMillis();
       //create a term to search file name
       Term term = new Term(LuceneConstants.FILE_NAME, searchQuery);
       //create the term query object
       Query query = new FuzzyQuery(term);
       searcher.setDefaultFieldSortScoring(true, false);
       //do the search
       TopDocs hits = searcher.search(query,Sort.INDEXORDER);
       long endTime = System.currentTimeMillis();
       System.out.println(hits.totalHits +
          " documents found. Time :" + (endTime - startTime) + "ms");
       for(ScoreDoc scoreDoc : hits.scoreDocs) {
          Document doc = searcher.getDocument(scoreDoc);
          System.out.print("Score: "+ scoreDoc.score + " ");
          System.out.println("File: "+ doc.get(LuceneConstants.FILE_PATH));
       }
       searcher.close();
    }