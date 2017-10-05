from rdflib import Namespace, Graph, URIRef, BNode, Literal
from rdflib.namespace import DCTERMS, RDFS, RDF, DC, FOAF, SKOS
from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")

query = """
SELECT ?s ?property ?propertyLabel WHERE {
  ?property wikibase:claim ?s .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
        """
print(query)
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
seqO = dict()
for result in results["results"]["bindings"]:
    file = open("/tmp/sublime_snippets/"+result["s"]["value"].replace("http://www.wikidata.org/prop/", "")+".sublime-snippet", "w")
    snippet = "<snippet><content><![CDATA["
    snippet += result["s"]["value"].replace("http://www.wikidata.org/prop/", "")
    snippet += "]]></content><tabTrigger>"
    snippet += result["propertyLabel"]["value"]
    snippet += """
    </tabTrigger>
    <scope>source.shex</scope>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<!-- <tabTrigger>hello</tabTrigger> -->
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<!-- <scope>source.python</scope> -->
    </snippet>
    """
    file.write(snippet)
    file.close()