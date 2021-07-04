## Development life cycle with microservices ?

### Microservices
 - also known as the microservice architecture 
 - is an architectural style that structures an application as a collection of services that are listed below in features section

### Features
- Highly maintainable and testable
- Loosely coupled 
- Independently deployable 
- Organized around business capabilities
- Owned by a small team

` The microservice architecture enables the rapid, frequent and reliable delivery of large, complex applications. It also enables an organization to evolve its technology stack. `

![alt microservice demo example](https://microservices.io/i/Microservice_Architecture.png) </br>
<small> Microservice architecture example diagram [1.0] </small>

### Objective
The main objective for now is to present an explample that how to organize the code and follow the unit testing approach along with the development, keeping the aim in mind for ` building a bullet proof development cycle.

### Testing

#### Unit testing
Unit Testing is a software testing technique by means of which individual units of software i.e. group of computer program modules, usage procedures and operating procedures are tested to determine whether they are suitable for use or not. It is a testing method using which every independent modules are tested to determine if there are any issue by the developer himself. It is correlated with functional correctness of the independent modules.

` Note-  Unit testing is first level of testing done before integration testing. Unit testing is such type of testing technique that is usually performed by the developers `

#### Objective of Unit Testing
The objective of Unit Testing is:

- To isolate a section of code.
- To verify the correctness of code.
- To test every function and procedure.
- To fix bug early in development cycle and to save costs.
- To help the developers to understand the code base and enable them to make changes quickly.
- To help for code reuse.

![alt level of testing](https://media.geeksforgeeks.org/wp-content/uploads/20190418130125/Capture6661.jpg)
<small> Level of testing [1.1] </small>

#### Workflow of Unit Testing
![alt testing workflow](https://media.geeksforgeeks.org/wp-content/uploads/20190418130430/Capture884444.jpg)


#### Advantages of Unit Testing
- Unit Testing allows developers to learn what functionality is provided by a unit and how to use it to gain a basic understanding of the unit API.
- Unit testing allows the programmer to refine code and make sure the module works properly.
- Unit testing enables to test parts of the project without waiting for others to be completed.

#### Unit Testing Libraries/Tools:
- PHPUnit
- PyUnit
- Jtest etc.




