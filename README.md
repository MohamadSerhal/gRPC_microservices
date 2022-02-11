# Grpc microservices
In this project, multiple GRPC services are used to create a Library database.

## Library Service:
PORT: 50051   
DEPLOYED ON: python-grpc-image (built on python3-alpine)   
Functionalities: 
- Add Book to library: A Librarian can add a book to the database
- Update book in library: A Librarian can update a book in the database
- Delete book in library: A Librarian can remove a book from the database
- Get book: Returns a book (with specified name) from the database
- Get books as a list: Returns a list of books in alphabetical order. Implements pagination.

## User Service:
PORT: 50000   
DEPLOYED ON: python-grpc-image (built on python3-alpine)
Note: User service calls the Library service in it's api.  
Functionalities:
- Extra info: Gets a list of books and add extra info to it randomly. Implements pagination.
- Get price: Using the name of a book, it gets its price.

## Docker-Compose File:
Creates 3 containers:
- grpcLibray-container: Running on "50051:50051"
- grpcUser-container: Running on "50000:50000"
    - image: "mohamadserhal/grpcuser-image:latest"
    - container_name: "grpcUser-container"
- authentication-container: Running on "2000:2000". Go to localhost:2000/ui for swagger user interface.
    - image: "mohamadserhal/openapi-authentication-image:latest"
    - container_name: "authentication-container"