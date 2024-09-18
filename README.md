# Tkinter Timer 

## Tkinter 1 minute timer built using MVC Design Pattern

### Approach

- Model: manage the backend logic and communicate with view through controller
- View: manage the application's UI
- Controller: build the connection between model and view

### View

View consists of two elements:

- Start Button: the timer starts when clicked
- Timer Label: timer representing the time flow

Each of these two components need to communicate with the model (backend). For this reason, they use the controller.

### Model

Model manages the logic of the timer. 

Methods implemented for model:

- start() -> make the timer running
- countdown() -> decrease timer by 1 second
- reset() -> timer returns to the default state
- converter() -> convert seconds into a MM:SS string format

### Controller

Controller serves as a link between view and model. 
When the Start Button is clicked, it communicates with model to make the timer running and the countdown working. Then, when the countdown starts, it communicates with view to update Timer Label every second.