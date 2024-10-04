#!/bin/sh

: "${GRAPHDB_HOST:=localhost}"
: "${GRAPHDB_PORT:=7200}"


is_graphdb_infrastructure_running() {
    status=$(curl -s -o /dev/null -w "%{http_code}" \
        -X GET "http://${GRAPHDB_HOST}:${GRAPHDB_PORT}/rest/monitor/infrastructure" \
        -H 'accept: application/json'
    )

    if [ "$status" -eq 200 ]; then
        return 0  # Return 0 (success) if status is 200
    else
        return 1  # Return non-zero (failure) otherwise
    fi
}

is_repo_existing() {
    status=$(curl -s -o /dev/null -w "%{http_code}" \
        -X GET "http://${GRAPHDB_HOST}:${GRAPHDB_PORT}/rest/repositories/$1" \
        -H 'accept: application/json'
    )

    if [ "$status" -eq 200 ]; then
        echo "Found repository $1"
        return 0  # Return 0 (success) if status is 200
    else
        echo "Repository $1 not found."
        return 1  # Return non-zero (failure) otherwise
    fi

}

# Start GraphDB in the background
start_graphdb() {
    /opt/graphdb/dist/bin/graphdb &
}

# GraphDB takes a few seconds to startup
setup_repository() {
    echo "Waiting for GraphDB available on port ${GRAPHDB_PORT} ..."
    while ! is_graphdb_infrastructure_running; do   
        sleep 1
    done
    echo "Detected GraphDB, check if repository $1 does exist..."
    # Now Process B can proceed
    if ! is_repo_existing $1; then
        echo "Setup repository $1"
        repo_file="$1-repo.ttl"
        status_setup=$(curl -s -o /dev/null -w "%{http_code}" \
            -X POST \
            "http://${GRAPHDB_HOST}:${GRAPHDB_PORT}/rest/repositories" \
            -H 'Content-Type: multipart/form-data'\
            -F "config=@/opt/$repo_file;type=text/turtle"
        )
        if [ "$status_setup" -eq 201 ]; then
            echo "Setup of $1 successful!"
        else
            echo "Setup of $1 failed!"
        fi
    else
        echo "Repo $1 already exists. Skip setup"
    fi
}

start_graphdb
setup_repository ceis-dev-local

wait
