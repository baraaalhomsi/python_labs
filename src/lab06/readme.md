# LR-6 — Generics and Typing

## 1. Purpose of the Work

The purpose of this laboratory work is to:
- Master the type annotation system in Python (typing)
- Learn to create generic classes using TypeVar and Generic
- Understand the concept of structural typing through typing.Protocol

## 2. Description of Implemented Types and Containers

### Generic Class TypedCollection

A universal container `TypedCollection[T]` has been implemented that:
- Supports adding, removing, and retrieving elements
- Preserves type information of stored elements
- Provides functional programming methods: `find`, `filter`, `map`
- Contains all methods of the original `Library` class from LR-2

### TypeVar and Constraints

- `T` — main TypeVar for collection elements
- `R` — second TypeVar for the `map` method, allowing result type to change
- `D = TypeVar('D', bound=Displayable)` — constrained by the Displayable protocol
- `S = TypeVar('S', bound=Scorable)` — constrained by the Scorable protocol

### Protocols

1. **Displayable** — describes objects with a `display_info() -> str` method
2. **Scorable** — describes objects with a `calculate_price_with_tax() -> float` method

The classes `PrintedBook`, `EBook`, and `AudioBook` conform to both protocols without explicit inheritance from them (structural typing).

## 3. Demonstration of Operation

### Scenario 0: Basic Usage of TypedCollection

Demonstrates creating a typed collection `TypedCollection[Student]`, adding objects, searching, filtering, and transforming using `map`.

![alt text](/images/lab06/Screenshot%202026-05-11%20133338.png)

### Scenario 1: TypedCollection[D] with Displayable Protocol

Shows that objects of different types (`PrintedBook`, `EBook`, `AudioBook`) are placed into the collection without explicit inheritance from the protocol. Protocol methods (`display_info()`) are called correctly for each type.

![alt text](/images/lab06/Screenshot%202026-05-11%20133402.png)

### Scenario 2: TypedCollection[S] with Scorable Protocol

Demonstrates using the same `TypedCollection` class with a different constraint (`Scorable`). Shows price calculations with tax for different book types.

![alt text](/images/lab06/Screenshot%202026-05-11%20133418.png)

## 4. Conclusion

During this laboratory work, the following were studied:
- Type annotations and their role in improving code reliability
- Generic classes and TypeVar for creating type-safe containers
- Protocols as a mechanism for structural typing
- Using bounds to create specialized collections

Typing significantly helps in reading and maintaining code by allowing errors to be detected at the development stage.