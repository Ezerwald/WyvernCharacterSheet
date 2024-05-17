# Coursework Paper: Wyvern Character Sheet

## 1. Introduction

### What is Wyvern Character Sheet?

The Wyvern Character Sheet is a web application designed to streamline the management of character sheets for players of the Dungeons and Dragons (D&D) tabletop role-playing game. It offers functionalities for creating, saving, and editing character sheets, automating calculations for modifiers, skill bonuses, hit points, and more.

### How to run the program?

To run the program, execute the `main.py` script from the repository. This will start the web server. Users can then access the website using a web browser.

### How to use the program?

Upon accessing the website, users can create, save, and edit character sheets. They can input various details such as character name, race, level, notes, and features. The program automatically calculates modifiers, skill bonuses, and other relevant statistics based on the input, simplifying the character management process.

## 2. Body/Analysis

### Functional Requirements Coverage

The Wyvern Character Sheet fulfills various functional requirements:

- **Creation and Management of Character Sheets:** Users can create, save, and edit character sheets with customizable details.
- **Automatic Calculations:** The program automates calculations for modifiers, skill bonuses, hit points, and other statistics, ensuring accuracy and efficiency.
- **Persistence:** Character sheets can be saved and loaded, allowing users to resume their progress at any time.
- **User-Friendly Interface:** The interface is designed to be intuitive and easy to navigate, enhancing the user experience.

### Technical Aspects and Design Patterns Used

The implementation leverages various technical aspects and design patterns to achieve functionality and maintainability:

- **Decorators:** `@property` and `@staticmethod` decorators are utilized to enhance method functionality and maintain code readability.
- **Composition Relation between Classes:** Composition is employed to establish relationships between classes, promoting modularity and code reuse.
- **Enumerations:** Enumerations are used to define constants representing various types, enhancing code clarity and maintainability.
- **Abstract Classes:** Abstract classes define common behavior and enforce structure among related classes, facilitating code organization and scalability.
- **Design Patterns:**
  - **Strategy Pattern:** Encapsulates algorithms for calculating skill bonuses based on character attributes, allowing for flexible selection at runtime.
  - **Factory Pattern:** Creates instances of character-related objects, promoting loose coupling and extensibility.
  - **Singleton Pattern:** Ensures that there is only one instance of the `CharacterSingleton` class throughout the application, providing global accessibility and consistency of character data.

## 3. Results and Summary

### Results

The Wyvern Character Sheet delivers accurate character sheets with all relevant details and calculations, empowering users to manage their characters efficiently and focus on gameplay.

### Conclusions

In conclusion, the Wyvern Character Sheet offers an efficient and user-friendly solution for managing D&D character sheets. By leveraging design patterns and technical aspects, the application ensures flexibility, maintainability, and extensibility.

### Future Extensions

The application can be extended by incorporating additional customization options for character details, implementing new features such as inventory management or combat tracking, and enhancing the user interface for improved usability and aesthetics.

## 4. Resources, references list

Libraries used: Flask

---
