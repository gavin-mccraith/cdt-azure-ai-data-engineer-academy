| Command | Purpose |
|----------|---------|
| docker pull | Download an image |
| docker run | Create a container |
| docker ps | Running containers |
| docker ps -a | All containers |
| docker stop | Stop a container |
| docker start | Start a container |
| docker rm | Remove a container |
| docker images | List images |
| docker rmi | Remove an image |
| docker logs | View logs |


| docker pull mcr.microsoft.com/mssql/server:2022-latest | Pull SQL 2022 image |

| docker run \
-e "ACCEPT_EULA=Y" \
-e "MSSQL_SA_PASSWORD=YourStrongPassword123!" \
-p 1433:1433 \
--name sql2022 \
-d mcr.microsoft.com/mssql/server:2022-latest | Run SQL server |

