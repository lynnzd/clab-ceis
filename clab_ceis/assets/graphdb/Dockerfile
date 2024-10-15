FROM ontotext/graphdb:10.7.3

COPY data/ceis-dev-local-repo.ttl /opt/ceis-dev-local-repo.ttl
COPY entrypoint.sh /opt/entrypoint.sh

RUN chmod 755 /opt/entrypoint.sh

# ENV GDB_JAVA_OPTS=" \
#     -Dgraphdb.home=/opt/graphdb/home \
#     -Dgraphdb.workbench.importDirectory=/opt/graphdb/home/graphdb-import \
#     -Dgraphdb.data=/opt/graphdb/home/data" 

# RUN mkdir -p /opt/graphdb/home/graphdb-import \
#     && /opt/graphdb/dist/bin/importrdf load \
#         --force -c ceis-dev-local-repo.ttl \
#         data

ENTRYPOINT [ "/opt/entrypoint.sh" ]