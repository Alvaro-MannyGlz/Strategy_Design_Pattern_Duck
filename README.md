# Strategy Design Pattern: Duck Simulator

This project implements the **Strategy Design Pattern** in Python to simulate various types of ducks with interchangeable behaviors. This architecture adheres to the **Open/Closed Principle (OCP)**, allowing new behaviors to be added without modifying the core duck classes.

---

## Assignment Objective: Decoupling Behaviors

The primary goal is to shift from rigid **inheritance** to flexible **composition** for the behaviors that change (Flying and Quacking/Sound).

| Principle Violated by Inheritance | Strategy Design Pattern Solution |
| :--- | :--- |
| **OCP Violation (Tight Coupling):** If you add a new flying method (e.g., FlyWithRocket), you must modify the base `Duck` class with an `if/else` block. | **Decoupling (Composition):** The `Duck` delegates the action to a **strategy object** it holds (e.g., `self.fly_behavior`). To add a new behavior, you only create a new class. |

---

## Duck Types and Behaviors

The simulation includes four concrete duck types, each composed of unique behavior strategies:

| Duck Type | Fly Strategy | Quack Strategy | Movement (Inheritance/Override) |
| :--- | :--- | :--- | :--- |
| **Mallard** | `FlyWithWings` | `LoudQuack` | Inherits standard `swim()` and `walk()` from the base `Duck`. |
| **San Antonio**| `FlyWithWings` | `QuackToBoat` | Inherits standard `swim()` and `walk()` from the base `Duck`. |
| **Rubber** | `NoFly` | `SquickSound` | **Overrides** `swim()` to float and `walk()` to be stationary. |
| **Decoy** | `NoFly` | `MuteQuack` | **Overrides** `swim()` and `walk()` to be stationary and unable to move. |

<img width="588" height="604" alt="image" src="https://github.com/user-attachments/assets/3c3eb9c2-22aa-4ae1-be52-8a84682115ac" />
