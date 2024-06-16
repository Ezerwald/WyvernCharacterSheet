# Coursework Paper: Wyvern Character Sheet

[![Wyvern Character Sheet Title](https://i.ibb.co/R6ZYbQC/2024-05-17-043257679.png)](https://ibb.co/C9Nm8Vn)


## 1. Introduction

### What is Wyvern Character Sheet?

The Wyvern Character Sheet is a web application designed to streamline the management of character sheets for players of the Dungeons and Dragons (D&D) tabletop role-playing game. It offers functionalities for creating, saving, and editing character sheets, automating calculations for modifiers, skill bonuses, hit points, and more.

### How to run the program?

To run the program, execute the `main.py` script from the repository. This will start the web server. Users can then access the website using a web browser.
(Later the website will be hosted on server and i will pin link here for free access and usage)

### How to use the program?

Upon accessing the website, users can create, save, and edit character sheets. They can input various details such as character name, race, level, notes, and features. The program automatically calculates modifiers, skill bonuses, and other relevant statistics based on the input, simplifying the character management process.

[![Wyvern Character Sheet Page](https://i.ibb.co/XpdL3XL/2024-05-17-043607798.png)](https://ibb.co/K7QhL6h)

Video Review

[![Watch the video](https://img.youtube.com/vi/jnw9LjEVXyI/hqdefault.jpg)](https://youtu.be/jnw9LjEVXyI?list=PLX3Xir0Xxxzydf0PvMXZhnTPPWYwl0L8q)

## 2. Body/Analysis

### Functional Requirements Coverage
The Wyvern Character Sheet fulfills various functional requirements:

- **Creation and Management of Character Sheets:** Users can create, save, and edit character sheets with customizable details.
- **Automatic Calculations:** The program automates calculations for modifiers, skill bonuses, hit points, and other statistics, ensuring accuracy and efficiency.
- **Persistence:** Character sheets can be saved and loaded, allowing users to resume their progress at any time.
- **User-Friendly Interface:** The interface is designed to be intuitive and easy to navigate, enhancing the user experience.
  
### Object-Oriented Programming (OOP) Pillars:
The project includes effective usage of OOP Pillars:
#### Encapsulation:
- bundling of data (attributes) and methods (behaviors) that operate on the data into a single unit, known as a class. It hides the internal state of an object from the outside world and only exposes a public interface for interacting with it.

#### Inheritance:
- mechanism by which a class can inherit properties and behavior from another class, known as the base or parent class. The class that inherits from the parent class is called a derived or child class. It promotes code reusability and establishes a hierarchical relationship between classes.

#### Polymorphism:
- allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent multiple underlying data types, allowing methods to behave differently based on the object they are invoked on.

#### Abstraction:
- simplifies complex systems by focusing on essential aspects while hiding unnecessary details. It allows us to model real-world entities as abstract data types, capturing only the relevant characteristics and behaviors.

### Technical Aspects and Design Patterns Used
The project was built using Flask, and the connection between the front-end and back-end is implemented with Ajax.

The implementation leverages various technical aspects and design patterns to achieve functionality and maintainability:

- **Composition Relation between Classes:** Composition is employed to establish relationships between classes, promoting modularity and code reuse.
- **Enumerations:** Enumerations are used to define constants representing various types, enhancing code clarity and maintainability.
- **Abstract Classes:** Abstract classes were used to define common behavior and enforce structure among related classes, facilitating code organization and scalability.
- **Design Patterns:**
  - **Strategy Pattern:** Encapsulates algorithms for calculating character's AC depending on his class, allowing for flexible selection at runtime.
  - **Factory Pattern:** Creates instances of character-related objects, promoting loose coupling and extensibility.
  - **Singleton Pattern:** Ensures that throughout the application there is only one instance of the `CharacterSingleton` class which is responsible for managing character's data, providing global accessibility and consistency of character data.
  - **Decorator Pattern:** `@property` and `@staticmethod` decorators are widely utilized to enhance methods functionality and maintain code readability.

## 3. Results and Summary

### Results:
- The implementation of various design patterns such as Strategy, Factory, and Singleton has significantly enhanced the modularity and scalability of the Wyvern Character Sheet application.
- Challenges were encountered during the integration of these patterns, particularly in ensuring seamless communication between different components of the application.
- Despite the challenges, the application now boasts improved maintainability and extensibility, allowing for easier implementation of new features and functionalities in the future.

### Conclusions:
- The Wyvern Character Sheet has achieved its primary objective of providing a user-friendly and efficient tool for managing D&D character sheets.
- The incorporation of design patterns and using SOLID principles has not only improved the technical robustness of the application but has also laid a solid foundation for future development and expansion.
- Moving forward, the program has the potential to evolve further by incorporating additional features, enhancing user experience, and addressing any remaining challenges to ensure continued success and relevance in the gaming community.


### Future Extensions
The application can be extended by incorporating additional customization options for character details, implementing new features such as inventory management or combat tracking, and enhancing the user interface for improved usability and aesthetics.

## 4. Resources, references list

Libraries used: Flask

---
