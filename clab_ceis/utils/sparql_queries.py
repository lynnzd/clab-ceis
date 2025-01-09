from SPARQLWrapper import SPARQLWrapper, JSON

SPARQL_ENDPOINT = "http://localhost:7200/repositories/clab-ceis"

def fetch_material():
    query = """
    PREFIX : <http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT 
        (STRAFTER(STR(?recipe), "http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/") AS ?recipeName)
        (STRAFTER(STR(?fabricBlockDesign), "http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/") AS ?fabricBlockDesignName)
        ?requiredAmount
        ?availableAmount
        (IF(?availableAmount >= ?requiredAmount, "Yes", "No") AS ?readyForAssembly)
    WHERE {
        # Link recipes to their requirements
        ?recipe :hasRequirement ?requirement .
        ?requirement :requiresFabricBlockDesign ?fabricBlockDesign .
        ?requirement :fabricBlockAmount ?requiredAmount .

        # Subquery to calculate available amount
        OPTIONAL {
            SELECT ?fabricBlockDesign (COUNT(?fabricBlock) AS ?availableAmount)
            WHERE {
                ?fabricBlock rdf:type :FabricBlock .
                ?fabricBlock :followsFabricBlockDesign ?fabricBlockDesign .
            }
            GROUP BY ?fabricBlockDesign
        }
    }

    """
    client = SPARQLWrapper(SPARQL_ENDPOINT)
    client.setQuery(query)
    client.setReturnFormat(JSON)
    try:
        # Query the endpoint and get results
        results = client.query().convert()  
        bindings = results['results']['bindings']
        
        data = [
            {
                'recipe': item['recipeName']['value'] if 'recipeName' in item else None,
                'fabricBlockDesign': item['fabricBlockDesignName']['value'] if 'fabricBlockDesignName' in item else None,
                'requiredAmount': int(item['requiredAmount']['value']) if 'requiredAmount' in item else 0,
                'availableAmount': int(item['availableAmount']['value']) if 'availableAmount' in item else 0,
                'readyForAssembly': item['readyForAssembly']['value'] if 'readyForAssembly' in item else "No"
            }
            for item in bindings
        ]

        # Debug: Print the parsed data
        print(data)

        return data

    except Exception as e:
        print(f"Error querying SPARQL endpoint: {e}")
        return []

def fetch_skirt_recipes():
    query = """
    PREFIX : <http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT 
        (STRAFTER(STR(?recipe), "http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/") AS ?recipeName)
        (STRAFTER(STR(?fabricBlockDesign), "http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/") AS ?fabricBlockDesignName)
        ?requiredAmount
        ?pdf
        WHERE {
        # Fetch recipes
        ?design rdf:type/rdfs:subClassOf* :SkirtDesign .
        ?recipe :isRecipeOf ?design .
        ?recipe :hasRequirement ?requirement .
        ?requirement :requiresFabricBlockDesign ?fabricBlockDesign .
        ?requirement :fabricBlockAmount ?requiredAmount .
        ?recipe :documentation ?pdf .
    }


    """
    client = SPARQLWrapper(SPARQL_ENDPOINT)
    client.setQuery(query)
    client.setReturnFormat(JSON)
    try:
        results = client.query().convert()
        bindings = results['results']['bindings']

        data = [
                {
                    # Make recipe name clickable with proper HTML formatting
                    'recipe': (
                        f"[{item['recipeName']['value']}]({item['pdf']['value']})"
                        if 'pdf' in item and 'recipeName' in item else None
                    ),

                    # Extract fabric block design name
                    'fabricBlockDesign': item['fabricBlockDesignName']['value'] 
                                        if 'fabricBlockDesignName' in item else None,

                    # Convert required amount to integer
                    'requiredAmount': int(item['requiredAmount']['value']) 
                                    if 'requiredAmount' in item else 0
                }
                for item in bindings
            ]


        print(data)
        return data

    except Exception as e:
        print(f"Error querying SPARQL endpoint: {e}")
        return []

def fetch_top_recipes():
    query = """
    PREFIX : <http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT 
        (STRAFTER(STR(?recipe), "http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/") AS ?recipeName)
        (STRAFTER(STR(?fabricBlockDesign), "http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/") AS ?fabricBlockDesignName)
        ?requiredAmount
        ?pdf
        WHERE {
        # Fetch recipes
        ?design rdf:type/rdfs:subClassOf* :TopDesign .
        ?recipe :isRecipeOf ?design .
        ?recipe :hasRequirement ?requirement .
        ?requirement :requiresFabricBlockDesign ?fabricBlockDesign .
        ?requirement :fabricBlockAmount ?requiredAmount .
        ?recipe :documentation ?pdf .
    }


    """
    client = SPARQLWrapper(SPARQL_ENDPOINT)
    client.setQuery(query)
    client.setReturnFormat(JSON)
    try:
        results = client.query().convert()
        bindings = results['results']['bindings']

        data = [
                {
                    # Make recipe name clickable with proper HTML formatting
                    'recipe': (
                        f"[{item['recipeName']['value']}]({item['pdf']['value']})"
                        if 'pdf' in item and 'recipeName' in item else None
                    ),

                    # Extract fabric block design name
                    'fabricBlockDesign': item['fabricBlockDesignName']['value'] 
                                        if 'fabricBlockDesignName' in item else None,

                    # Convert required amount to integer
                    'requiredAmount': int(item['requiredAmount']['value']) 
                                    if 'requiredAmount' in item else 0
                }
                for item in bindings
            ]


        print(data)
        return data

    except Exception as e:
        print(f"Error querying SPARQL endpoint: {e}")
        return []

def fetch_location():
    query = """
    PREFIX : <http://www.semanticweb.org/sophi/ontologies/2024/10/untitled-ontology-20/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?location ?fabricBlockDesign (COUNT(?fabricBlock) AS ?countAtLocation)
    WHERE {
    # Retrieve fabric blocks and their associated designs and locations
    ?fabricBlock rdf:type :FabricBlock .
    ?fabricBlock :followsFabricBlockDesign ?fabricBlockDesign .
    ?fabricBlock :hasLocation ?location .
    
    # Ensure the location is one of the specified ones
    FILTER (?location IN (:location1, :location2, :location3))
    }
    GROUP BY ?location ?fabricBlockDesign
    ORDER BY ?location ?fabricBlockDesign
    """
    client = SPARQLWrapper(SPARQL_ENDPOINT)
    client.setQuery(query)
    client.setReturnFormat(JSON)
    try:
        results = client.query().convert()
        print("Raw Results:", results)  # Debug raw results
        bindings = results['results']['bindings']
        print("Bindings:", bindings)  # Debug parsed bindings
        
        data = [
            {
                'location': item['location']['value'].split("/")[-1] if 'location' in item else None,
                'fabricBlockDesign': item['fabricBlockDesign']['value'].split("/")[-1] if 'fabricBlockDesign' in item else None,
                'countAtLocation': int(item['countAtLocation']['value']) if 'countAtLocation' in item else 0
            }
            for item in bindings
        ]

        print("Processed Data:", data)  # Debug final data
        return data

    except Exception as e:
        print(f"Error querying SPARQL endpoint: {e}")
        return []