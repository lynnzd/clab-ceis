import os
import requests
import sys

def run_sparql_query(query_file):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the base directory for the query files relative to the script location
    query_file_path = os.path.join(script_dir, query_file)

    # Check if the query file exists
    if not os.path.isfile(query_file_path):
        print(f"Query file '{query_file_path}' not found.")
        return

    # Load the SPARQL query from file
    try:
        with open(query_file_path, 'r') as file:
            sparql_query = file.read()
    except FileNotFoundError:
        print(f"Query file '{query_file_path}' not found.")
        return

    # GraphDB Server and repository settings
    graphdb_url = "http://localhost:7200/repositories/clab-ceis"

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
    # Check for the query file argument
    if len(sys.argv) != 2:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Navigate to this directory before running: {script_dir}")
        print("Run in terminal using this command: python run_query.py <query_file.rq>")
        sys.exit(1)

    # Get the query file from the command line argument
    query_file = sys.argv[1]
    run_sparql_query(query_file)