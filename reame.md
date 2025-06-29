netstat -an| findstr 6333
#linux
netstat -tuln | grep :8080
#start docker desktop 
    docker pull qdrant/qdrant
 docker run -d --name qdrant -p 6333:6333 -v D:\Python_Projects\RAG\qdrant_storage:/qdrant/storage qdrant/qdrant
 docker ps 

 # Check if container is running
docker ps

# View container logs
docker logs qdrant

# Follow logs in real-time
docker logs -f qdrant

# Check container details
docker inspect qdrant

# to install qdrant  apt update && apt install -y curl