
## Deploy Opensearch by Docker image

https://github.com/jerryjliu/llama_index >> examples/vector_indices/OpensearchDemo.ipynb

```commandline
docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -e "plugins.security.disabled=true" opensearchproject/opensearch:latest
```

Kibana (Open search Dashboard) may need to be configured with docker-compose.

```commandline
docker-compose up -d
```

--detach , -d		Detached mode: Run containers in the background

https://github.com/opensearch-project/opensearch-build/blob/main/docker/release/README.md

```commandline
2023-04-03 17:27:19 org.opensearch.bootstrap.StartupException: OpenSearchException[failed to bind service]; nested: AccessDeniedException[/usr/share/opensearch/data/nodes];
2023-04-03 17:27:19     at org.opensearch.bootstrap.OpenSearch.init(OpenSearch.java:184) ~[opensearch-2.6.0.jar:2.6.0]
2023-04-03 17:27:19     at org.opensearch.bootstrap.OpenSearch.execute(OpenSearch.java:171) ~[opensearch-2.6.0.jar:2.6.0]
2023-04-03 17:27:19     at org.opensearch.cli.EnvironmentAwareCommand.execute(EnvironmentAwareCommand.java:104) ~[opensearch-2.6.0.jar:2.6.0]
2023-04-03 17:27:19     at org.opensearch.cli.Command.mainWithoutErrorHandling(Command.java:138) ~[opensearch-cli-2.6.0.jar:2.6.0]
2023-04-03 17:27:19     at org.opensearch.cli.Command.main(Command.java:101) ~[opensearch-cli-2.6.0.jar:2.6.0]
2023-04-03 17:27:19     at org.opensearch.bootstrap.OpenSearch.main(OpenSearch.java:137) ~[opensearch-2.6.0.jar:2.6.0]
2023-04-03 17:27:19     at org.opensearch.bootstrap.OpenSearch.main(OpenSearch.java:103) ~[opensearch-2.6.0.jar:2.6.0]
```

## Opensearch Troubleshooting

https://stackoverflow.com/questions/65668188/elastic-search-accessdeniedexception-usr-share-elasticsearch-data-nodes-0-a

https://stackoverflow.com/questions/70759246/unable-to-get-opensearch-dashboard-by-running-opensearch-docker-compose

## Force-recreate Docker Image

```commandline
docker-compose up --force-recreate --build -d
docker image prune
```