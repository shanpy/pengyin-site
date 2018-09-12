.. title: RDF Basics
.. date: 2015-07-21
.. modified: 2015-08-03
.. category: Others
.. tags: Digital Library, Search Engine, Research, Data
.. slug: rdf-basics
.. authors: Pengyin Shan
.. description: This posts includes basic knowledge I found online about RDF(Resource Description Framework), a standard from W3C to describe resources.

###Resource

<a href="http://www.w3schools.com/webservices/ws_rdf_intro.asp">Introduction to RDF From W3C</a>

###Intro to RDF

RDF (Resource Description Framework) is standard from W3C to describe describe title, author, content, and copyright information of web pages.

It is really useful for search engines or digital library.

####Realities of RDF

- RDF is designed to be read and understood by computers, instead ofbeing displayed to people. *RDF descriptions are not designed to be displayed on the web*.

- RDF is written in **XML**

- RDF is a part of the W3C's Semantic Web Activity

- RDF is a **W3C Recommendation**

>W3C's **Semantic Web Version** has following features:
>
>	- Web information has exact meaning
>
>	- Web information can be understood and processed by computers
>
>	- Computers can integrate information from the web

###RDF Rules

RDF identifies things using **Web identifiers** (URIs), and describes resources with **properties** and **property values**.

- `Resource`:  anything that can have a `URI`

- `Property`: a Resource that has a **name**, such as "author" or "homepage"

- `Property value`: the **value** of a Property

Example From W3C:

	:::xml
	<?xml version="1.0"?>
	<RDF>
	  <Description about="http://www.w3schools.com/rdf">
	    <author>Jan Egil Refsnes</author>
	    <homepage>http://www.w3schools.com</homepage>
	  </Description>
	</RDF>

###RDF Statements

The **combination** of a `Resource`, a `Property`, and a `Property value` forms a `Statement` .

- Resource is the `subject` of Statement

- Property is the `predicate` of Statement

- Property value is the `object` of Statement.

Example from W3C:

- Statement: "The author of http://www.w3schools.com/rdf is Jan Egil Refsnes".

- Subject: http://www.w3schools.com/rdf

- Predict: author

- Object: Jan Egil Refsnes

###RDF Main Elements

A full RDF example with from W3C:

	:::xml
	<?xml version="1.0"?>
	<!-- Declare RDF -->
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:cd="http://www.recshop.fake/cd#">
		<!-- Start of a Description. rdf:about contains the description of resource -->
		<rdf:Description rdf:about="http://www.recshop.fake/cd/Empire Burlesque">
			<!-- following cd items are properties of resource, with property values -->
			  <cd:artist>Bob Dylan</cd:artist>
			  <cd:country>USA</cd:country>
			  <cd:company>Columbia</cd:company>
			  <cd:price>10.90</cd:price>
			  <cd:year>1985</cd:year>
		</rdf:Description>
		<rdf:Description rdf:about="http://www.recshop.fake/cd/Hide your heart">
			  <cd:artist>Bonnie Tyler</cd:artist>
			  <cd:country>UK</cd:country>
			  <cd:company>CBS Records</cd:company>
			  <cd:price>9.90</cd:price>
			  <cd:year>1988</cd:year>
		</rdf:Description>
	</rdf:RDF>


The main elements of RDF are:

1. `<rdf:RDF>` root element

2. `<RDF>` element

3. `<Description>` element

####<rdf:RDF>

`<rdf:RDF>` is the root element of an RDF document.

It defines the XML document to be an RDF document.

It also contains a reference to the RDF namespace.

####<rdf:Description>

The `<rdf:Description>` element identifies a resource with the `about` attribute.

The `<rdf:Description>` element contains elements that *describe* the resource.

####<cd>

Elements with `<cd>` namespace is not part of RDF. RDF defines only the framework.

So the elements, artist, country, company, price, and year, *must be defined by someone else* (company, organization, person, etc).

You can also define these **properties as attributes** of `<rdf:Description>`. For example:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:cd="http://www.recshop.fake/cd#">
		<rdf:Description
		rdf:about="http://www.recshop.fake/cd/Empire Burlesque"
		cd:artist="Bob Dylan" cd:country="USA"
		cd:company="Columbia" cd:price="10.90"
		cd:year="1985" />
	</rdf:RDF>

You can also define these **properties as resources** of `<rdf:Description>`. For example:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:cd="http://www.recshop.fake/cd#">
		<rdf:Description rdf:about="http://www.recshop.fake/cd/Empire Burlesque">
		    <cd:artist rdf:resource="http://www.recshop.fake/cd/dylan" />
		    <!-- other rdf:resource with cd namespace -->
		</rdf:Description>
	</rdf:RDF>

###RDF Container Elements

RDF containers are used to describe **group of things**.

The following RDF elements are used to describe groups: `<Bag>`, `<Seq>`, and `<Alt>`.

###<rdf:Bag>

The `<rdf:Bag>` element is used to describe a list of values that *do not have to be in a specific order*.

The `<rdf:Bag>` element *may contain duplicate values*.

Example from W3C:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:cd="http://www.recshop.fake/cd#">
		<rdf:Description
		rdf:about="http://www.recshop.fake/cd/Beatles">
		  <cd:artist>
		    <rdf:Bag>
		      <rdf:li>John</rdf:li>
		      <rdf:li>Paul</rdf:li>
		      <rdf:li>George</rdf:li>
		      <rdf:li>Ringo</rdf:li>
		    </rdf:Bag>
		  </cd:artist>
		</rdf:Description>
	</rdf:RDF>

###<rdf:Seq>

The `<rdf:Seq>` element is used to describe an *ordered list of values* (For example, in alphabetical order).

The `<rdf:Seq>` element *may contain duplicate values*.

If you want to see an example, just replace `<rdf:Bag>` with `<rdf:Seq>` from example abpve.

###<rdf:Alt>

The `<rdf:Alt>` element is used to describe a list of alternative values (*the user can select only one of the values*).

Example from W3C:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:cd="http://www.recshop.fake/cd#">
		<rdf:Description
		rdf:about="http://www.recshop.fake/cd/Beatles">
			  <cd:format>
			    <rdf:Alt>
			      <rdf:li>CD</rdf:li>
			      <rdf:li>Record</rdf:li>
			      <rdf:li>Tape</rdf:li>
			    </rdf:Alt>
			  </cd:format>
		</rdf:Description>
	</rdf:RDF>

####RDF Terms

- A `container` is a resource that contains things

- The contained things are called `member`s (not list of values)

###RDF Collections

RDF collections describe groups that can **ONLY** contain the specified members.

A collection is described by the attribute `rdf:parseType="Collection"`.

Example from W3C:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:cd="http://recshop.fake/cd#">
		<rdf:Description
		rdf:about="http://recshop.fake/cd/Beatles">
			  <!-- This cd namespace element contains a series of rdf description elements -->
			  <cd:artist rdf:parseType="Collection">
				    <rdf:Description rdf:about="http://recshop.fake/cd/Beatles/George"/>
				    <rdf:Description rdf:about="http://recshop.fake/cd/Beatles/John"/>
				    <rdf:Description rdf:about="http://recshop.fake/cd/Beatles/Paul"/>
				    <rdf:Description rdf:about="http://recshop.fake/cd/Beatles/Ringo"/>
				  </cd:artist>
		</rdf:Description>
	</rdf:RDF>

###RDF Schema (RDFS)

RDF Schema does not provide actual application-specific classes and properties.

Instead RDF Schema provides **the framework to describe** application-specific classes and properties.

*Classes in RDF Schema are much like classes in object oriented programming languages*. This allows resources to be defined as instances of classes, and subclasses of classes.

Example from W3C:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
	xml:base="http://www.animals.fake/animals#">
		<rdf:Description rdf:ID="animal">
		  	<rdf:type rdf:resource="http://www.w3.org/2000/01/rdf-schema#Class"/>
		</rdf:Description>
		<rdf:Description rdf:ID="horse">
		  	<rdf:type rdf:resource="http://www.w3.org/2000/01/rdf-schema#Class"/>
			<!-- Note the resource "horse" is a subclass of the class "animal"-->
		  <rdfs:subClassOf rdf:resource="#animal"/>
		</rdf:Description>
	</rdf:RDF>

The example above can be abbreviated to:

	:::xml
	<?xml version="1.0"?>
	<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
	xml:base="http://www.animals.fake/animals#">
		<rdfs:Class rdf:ID="animal" />
		<rdfs:Class rdf:ID="horse">
			  <!-- Define the resource "horse" is a subclass of the class "animal"-->
			  <rdfs:subClassOf rdf:resource="#animal"/>
		</rdfs:Class>
	</rdf:RDF>

###OWL

OWL is a language for processing web information. It is built on top of RDF, and also written in `XML`.

`Ontology` is about the exact description of things and their relationships.

For the web, ontology is about the exact description of web information and relationships between web information.

OWL and RDF are much of the same thing, but OWL is a **stronger** language with greater machine interpretability than RDF.

OWL comes with a larger vocabulary and stronger syntax than RDF.

OWL is also a W3C recommendation.