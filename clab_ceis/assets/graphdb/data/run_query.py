import os
import requests

def run_sparql_query():
    # Print out the script's directory for debugging purposes
    script_dir = os.path.dirname(__file__)  # Get the directory of the current script
    print("Script directory:", script_dir)

    # GraphDB Server and repository settings
    graphdb_url = "http://localhost:7200/repositories/clab-ceis"
    query_file_path = os.path.join(script_dir, "garment_query.rq")  # Absolute path to the query file

    # Load the SPARQL query from file
    try:
        with open(query_file_path, 'r') as file:
            sparql_query = file.read()
    except FileNotFoundError:
        print(f"Query file '{query_file_path}' not found.")
        return

    # Headers for SPARQL query request
    headers = {
        "Content-Type": "application/sparql-query"
    }

    # Send the query to GraphDB
    try:
        response = requests.post(graphdb_url, data=sparql_query, headers=headers)

        # Check for successful response
        if response.status_code == 200:
            print("Query executed successfully!")
            print("Response:")
            print(response.text)
        else:
            print(f"Query failed with status code {response.status_code}")
            print("Error:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error executing query:", e)

# Run the function if the script is executed directly
if __name__ == "__main__":
    run_sparql_query()
