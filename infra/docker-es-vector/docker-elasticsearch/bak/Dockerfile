FROM docker.elastic.co/elasticsearch/elasticsearch:8.7.0
RUN bin/elasticsearch-plugin remove analysis-kuromoji
RUN bin/elasticsearch-plugin install analysis-kuromoji
RUN bin/elasticsearch-plugin remove analysis-icu
RUN bin/elasticsearch-plugin install analysis-icu