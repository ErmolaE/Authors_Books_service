# Authors_Books_service
A compact web service that allows you to work with authors and books.


About
-----

The service provides an interface for working with such an entity as “BOOK”.
You can save book information by sending an HTTP request to the service.
You can get information about saved books by sending an HTTP request to the service.
The service provides an interface for working with such an entity as “AUTHOR”.
You can save information about the author by sending an HTTP request to the service.
You can get information about saved authors by sending an HTTP request to the service.
The entities “BOOK” and “AUTHOR” are connected by relationships: a book can be written by several (1 or more) authors. An author can write 0 or many books.



start: docker-compose up -d