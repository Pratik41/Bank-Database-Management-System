
# Device Farm

## Description

- **InventoryManagementService**
 
    This is a Spring Boot Service implemented with runtime as Java 1.8. Basic functionalities of this app includes CRUD operations of Server, Device, Browser, Client and other Devices. Spring Boot Security has been enabled, for Authentication and Authorization JWT token with role based access has been implemented. It has emailing mechanism implemented with which clients can be able to see the reports generated. Application uses Mongodb as primary database to store, read and write different documents.
   
   - This link contains contract of each API’s:-[Contract of API’s](http://34.197.100.75:32174/swagger-ui.html)

- **InventoryManagementUI**

   A frontend application implemented in Angular and typescript. It has multiple screens namely **Server**, **Device**, **Browser**, **Client** and **Other Devices** for all CRUD related activities. Dashboard screen which generates an analytical sense of recorded data. A **Metaverse** page to show all the nodes and relations of different entities (work in progress). All the operations are enriched with suggestion where user has less overhead in deciding and typing the things. All the actions are based on the roles of the user logged in.
## Prerequisties

- Java 1.8
- Maven
- NodeJS
- MongoDB
- Postman
- IDE(Visual Studio,Eclipse/STS)
## Getting Started
- #### For Setting up the Backend Services
  - To clone the project from Github run

    ```bash
    git clone https://github.com/tejakathari007/Inventory-Management
    ```
  - To move into the particular directory of the project run
    ```bash
    cd InventoryManagementService 
    ```
  - To do maven build and run the SpringBoot Application follow the below commands respectively run
    ```bash
    mvn clean install
    mvn spring-boot:run
    ```
- #### For Setting up the FrontEnd project
  - To move into the particular directory of the project run
    ```bash
    cd ..
    cd InventoryManagementUI 
    ```
  - To install all the dependencies of a project run
    ```bash
    npm install
    ```
  - To build all the file changes and serve it locally run
    ```bash
    ng serve
    ```
**NOTE** : Property files of spring boot, environment file of Angular app needs to be updated with required credentials.


## Deployment Procedure

- There is Jenkins script available in each of the applications to build them.
- There is Docker file available in each of the applications which helps in creating the docker image and push it to the registry.
- Cloud Formation template is attached which helps in deploy the application and related dependents.


## API Reference

- There are two roles which was being created : **ROLE_ADMIN**,**ROLE_EDITOR**
- Use **Access Tokens** to keep users authenticated across requests.

  ### Design and build the following endpoints.

  - #### To register Admin or User

    | Method | Endpoint      | Description                                                                                                                                                                                                                                                            |
    | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | POST   | /user         | To sign-up as `user`or `admin` send userName,password and role accordingly based on `user` and `admin`.                                                                                                                            |
    | POST   | /auth/login   | Send the correct userName and password inside the body to get correct the AccessToken accordingly.                                                                                                                                                                                                                            |

  - #### CRUD Operation for Server

    | Method | Endpoint      | Description                                                                                                                                                                                                                                                            |
    | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | POST   | /inventory/v1/addServer        | To add new server send all the required inputs inside body.                                                                                                                            |
    | PUT   | /inventory/v1/updateServer  | To update existing server add the required changes and send all the required inputs inside body.                                                                                                                                                                                                                            |
    | GET   | /inventory/v1/getAllServers       | To get all the servers related details.                                                                                                                            |
    | GET   | /inventory/v1/getServer/{serverId}  | To get the servers related details based on `serverId`.                                                                                                                                                                                                                            |
    | DELETE   | /inventory/v1/deleteServer/{serverId}  | To delete the servers related details based on `serverId`.                                                                                                                                                                                                                            |

  - #### CRUD Operation for Client

    | Method | Endpoint      | Description                                                                                                                                                                                                                                                            |
    | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | POST   | /inventory/v1/addClient        | To add new client send all the required inputs inside body.                                                                                                                            |
    | PUT   | /inventory/v1/updateClient  | To update existing client add the required changes and send all the required inputs inside body.                                                                                                                                                                                                                            |
    | GET   | /inventory/v1/getAllClients       | To get all the client related details.                                                                                                                            |
    | GET   | /inventory/v1/getClient/{clientId}  | To get the client related details based on `clientId`.                                                                                                                                                                                                                            |
    | DELETE   | /inventory/v1/deleteClient/{clientId}  | To delete the servers related details based on `serverId`.                                                                                                                                                                                                                            |

  - #### CRUD Operation for Device

    | Method | Endpoint      | Description                                                                                                                                                                                                                                                            |
    | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | POST   | /inventory/v1/addDevice        | To add new device send all the required inputs inside body.                                                                                                                            |
    | PUT   | /inventory/v1/updateDevice  | To update existing device add the required changes and send all the required inputs inside body.                                                                                                                                                                                                                            |
    | GET   | /inventory/v1/getAllDevices       | To get all the device related details.                                                                                                                            |
    | GET   | /inventory/v1/getDevice/{deviceId}  | To get the device related details based on `deviceId`.                                                                                                                                                                                                                            |
    | DELETE   | /inventory/v1/deleteDevice/{deviceId}  | To delete the device related details based on `deviceId`.                                                                                                                                                                                                                            |

  - #### CRUD Operation for Browser

    | Method | Endpoint      | Description                                                                                                                                                                                                                                                            |
    | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | POST   | /inventory/v1/addBrowser        | To add new browser send all the required inputs inside body.                                                                                                                            |
    | PUT   | /inventory/v1/updateBrowser  | To update existing browser add the required changes and send all the required inputs inside body.                                                                                                                                                                                                                            |
    | GET   | /inventory/v1/getAllBrowsers       | To get all the browser related details.                                                                                                                            |
    | GET   | /inventory/v1/getBrowser/{browserId}  | To get the browser related details based on `browserId`.                                                                                                                                                                                                                            |
    | DELETE   | /inventory/v1/deleteBrowser/{browserId}  | To delete the browser related details based on `browserId`.                                                                                                                                                                                                                            |

  - #### CRUD Operation for Others

    | Method | Endpoint      | Description                                                                                                                                                                                                                                                            |
    | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | POST   | /inventory/v1/addOtherDevices        | To add new OtherDevices send all the required inputs inside body.                                                                                                                            |
    | PUT   | /inventory/v1/updateOtherDevices   | To update existing OtherDevices add the required changes and send all the required inputs inside body.                                                                                                                                                                                                                            |
    | GET   | /inventory/v1/getAllOtherDevices        | To get all the OtherDevices related details.                                                                                                                            |
    | GET   | /inventory/v1/getOtherDevices /{oDeviceId}  | To get the OtherDevices related details based on `oDeviceId`.                                                                                                                                                                                                                            |
    | DELETE   | /inventory/v1/deleteOtherDevices/{oDeviceId}  | To delete the OtherDevices related details based on `oDeviceId`.                                                                                                                                                                                                                            |
    
  **NOTE** : ROLE_ADMIN can only delete the Server,Browser,Client,Devices & Others.    
