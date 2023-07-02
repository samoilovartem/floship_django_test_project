# Floship test task

This project features a Django application composed of two separate parts: the Store and the Warehouse. The goal is to ensure synchronization between the Store and Warehouse databases, reflecting changes in one system onto the other.

## Main Features

### Store
- A user can create, update, or delete a `StoreOrder` from the Store app.
- When a `StoreOrder` is created or updated the changes are automatically reflected in the corresponding `WarehouseOrder` in the Warehouse app.
- The Store application uses Django signals to detect when a `StoreOrder` object is created, updated, or deleted, triggering the appropriate API calls to the Warehouse app.

### Warehouse
- Similar to the Store, a user can create or update `WarehouseOrder` from the Warehouse app.
- Changes to a `WarehouseOrder` are also synchronized back to the corresponding `StoreOrder` in the Store app.
- This synchronization process is implemented using Django viewset methods to handle the creation and update of `WarehouseOrder` objects, which in turn trigger the appropriate API calls to the Store app.

## Synchronization Logic
To prevent infinite loops (deadlocks) of updates between the two applications, a sync field is included in both the `StoreOrder` and `WarehouseOrder` models. This field indicates whether an update should be propagated to the other app or not. This is particularly useful when the update is initiated by the corresponding application to prevent a deadlock situation.

## API Endpoints
The project includes API endpoints for creating, retrieving, updating, and deleting `StoreOrder` and `WarehouseOrder` objects.

## Future improvements
- Implement delete sync functionality.
- Implement authentication and authorization for the API endpoints.
- Use async features or Celery for handling heavy operations and improving performance.
- Add unit tests and integration tests to ensure code reliability and maintainability.

## How to Run the Project

### Clone the repository and rename .env.example to .env

First, clone this repository to your local machine.
```shell
git clone https://github.com/samoilovartem/floship_django_test_project.git
```
Then simply rename file `.env.example` to `.env`.

### Build and run the containers

This project uses Docker Compose to manage the Docker containers for the Django applications and the PostgreSQL databases.

To start the project, simply run the following command in the terminal:
```shell
docker-compose up --build
```
Note: no need to apply migrations manually, `entrypoint.sh` will do the job.

### Create superuser

You need to create a superuser to access admin dashboard and test sync functionality. Just run the following commands and follow instructions from Django:
```shell
docker exec -it django sh
python manage.py createsuperuser
```
