docker build -t pgstreamlit .
docker run --publish 8501:8501 -it --rm  --name pgstreamlit pgstreamlit

