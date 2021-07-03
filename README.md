## User micro-services

` Project Setup`
```
Prerequisite;
```
Install docker and docker-compose in your OS
</br> 
please refere the <a href="https://docs.docker.com/engine/install/ubuntu/">Link</a>

```
 Up/Running with service
 ```
 <ul>
    <li> Go to project root directory </li>
    <li> To start project: Run <b> docker-compose up -d </b> </li>
    -   now visit on http://127.0.0.1:8000 </br>
    - Note: Make sure port 8000 and 5432 is open in your machine
    <li> To stop your project: Run <b>docker-compose down</b> </li>
 </ul>

```
Troubleshoot
```
In case of any issue run command with sudo or take reference of log
</br>
To view container log
</br>
Run: docker logs ##container-name##
</br>
Or 
</br>
RUN: docker-compose down and then docker-compose up
now see the log in terminal


</br>
Anuj Kumar Singh</br>
anuj.dev@hotmail.com
Happy to help you !!