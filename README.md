- docker build -t no_context_docker .       -> docker build
- docker run -p 8000:8000 no_context_docker -> 8000 portu üzerinden container yaratılıyor


Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  2YmbWtfS+JIAAFPrhVf7

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  725978c29fee1ee57085c7817bbec2b30a2fc80021972689de64af84174ef7cc

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjEyLjAiLCJhZHIiOlsiMTkyLjE2OC4xLjQ2OjkyMDAiXSwiZmdyIjoiNzI1OTc4YzI5ZmVlMWVlNTcwODVjNzgxN2JiZWMyYjMwYTJmYzgwMDIxOTcyNjg5ZGU2NGFmODQxNzRlZjdjYyIsImtleSI6ImpMQjFOWTBCek4wMml5bFZtTEdnOl9MN0tkcllmUnRlbENSMnRSaW5Za2cifQ==

ℹ️  Configure other nodes to join this cluster:
• On this node:
  ⁃ Create an enrollment token with `bin/elasticsearch-create-enrollment-token -s node`.
  ⁃ Uncomment the transport.host setting at the end of config/elasticsearch.yml.
  ⁃ Restart Elasticsearch.
• On other nodes:
  ⁃ Start Elasticsearch with `bin/elasticsearch --enrollment-token <token>`, using the enrollment token that you generated.



 Kibana has not been configured.

Go to http://localhost:5601/?code=243162 to get started.