<a id="readme-top"></a>

<br />
<div align="center">
  <a href="#">
    <img src="assets/server.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Http server</h3>

  <p align="center">
    Simple HTTP server to share files on network.
    <br />
    <br />
  </p>
</div>

## About The Project

Network programming is often overlooked in traditional education, leaving many developers with limited understanding of how data flows through systems and networks. Without knowledge of protocols and their behavior, it can be challenging to grasp the intricacies of data transmission.

The goal of this project is to provide a simple Python-based server for file sharing within the same network. This can be especially useful in scenarios such as enabling teachers to easily share resources with their students.

## Definition of Done

This project will be considered as done once the following requirements are fullfilled.

- A server can be started and can accept any connections on the same network.
- Data can be shared from the same network to any devices trying to connect (laptop, phone, desktop).
- DOS control is implemented in order to prevent a specific machine to attempt multiple connexion in a small period of time.

## Note

This project uses high level helpers from http.server python package and does not implement functions directly using sockets.
For more informations on how sockets works, here is a documentation link : https://medium.com/@stephen.biston/write-an-http-server-from-the-ground-up-in-9-minutes-with-python-1fdb9800a26a
