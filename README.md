# Adopt a Pet

This project is a web application built using Flask. It was created as a part of the Webserverprogramming 1 course during the 23/24 curriculum at NTI Gymnasiet. The website serves as a mock-up of a pet adoption platform, featuring a variety of animals such as dogs, cats, and rabbits that are available for adoption. The application leverages a separate helper.py file for storing pet data and provides distinct routes for users to browse pets by type and view detailed information about individual pets.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

This project is a sophisticated web application built using Flask. It was created as part of the Web Server Programming 1 course during the 23/24 curriculum at NTI Gymnasiet. The website serves as a prototype for a pet adoption platform, where a variety of animals such as dogs, cats, and rabbits are available for adoption.

The application leverages a separate helper.py file to store pet data. This file acts as a database and contains all necessary information about the available pets, including their names, ages, breeds, and more.

The website offers several distinct routes for users to interact with, including:

/: The homepage that displays all available pets for adoption.
/dogs: A page that displays all available dogs for adoption.
/cats: A page that displays all available cats for adoption.
/rabbits: A page that displays all available rabbits for adoption.
/pet/<pet_id>: A detailed page for each pet, where users can view more information about the specific pet.
By using these routes, users can easily browse pets by type and view detailed information about each individual pet. This makes it easy for potential adopters to find the perfect pet for them.

## Features

The key features of the project are:

A web application built using Flask.
A mock-up of a pet adoption platform.
Supports adoption of dogs, cats, and rabbits.
Utilizes a separate helper.py file for storing pet data.
Provides distinct routes for browsing pets by type.
Detailed information about individual pets.
Easy navigation for potential adopters to find the perfect pet.

## Installation

To get the application up and running, execute the following steps:

1. Clone the repository onto your local machine.
2. Change your directory to the project's root folder.
3. Install the necessary dependencies by executing:
       pip install -r requirements.txt
4. Launch the application by running:
       python app.py
5. Access the application by opening http://localhost:5000 in your preferred web browser.

## Usage

To use the project, follow these steps:

1. Clone the repository onto your local machine.
2. Change your directory to the project's root folder.
3. Install the necessary dependencies by executing:
    ```
    pip install -r requirements.txt
    ```
4. Launch the application by running:
    ```
    python app.py
    ```
5. Access the application by opening http://localhost:5000 in your preferred web browser.

Once the application is running, you can interact with it using the following routes:

- `/`: This is the homepage that displays all available pets for adoption.
- `/dogs`: This page shows all available dogs for adoption.
- `/cats`: This page shows all available cats for adoption.
- `/rabbits`: This page shows all available rabbits for adoption.
- `/pet/<pet_id>`: This is a detailed page for each pet, where you can view more information about the specific pet.

By using these routes, users can easily browse pets by type and view detailed information about each individual pet. This makes it convenient for potential adopters to find the perfect pet for them.

## License

This project is licensed under the MIT license. see the [LICENSE](LICENSE) file for details



