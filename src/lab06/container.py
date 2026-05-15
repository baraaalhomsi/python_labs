from typing import TypeVar, Generic, Callable, Optional, Protocol, List

T = TypeVar('T')
R = TypeVar('R')

class Displayable(Protocol):
    def display_info(self) -> str:
        ...

class Scorable(Protocol):
    def calculate_price_with_tax(self) -> float:
        ...

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        if not isinstance(item, object):
            raise TypeError(f"Cannot add {type(item).__name__}.")
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Index {index} out of range. Collection has {len(self._items)} items.")
        return self._items.pop(index)
    
    def get_all(self) -> List[T]:
        return self._items.copy()
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index) -> T:
        if isinstance(index, int):
            if index < 0 or index >= len(self._items):
                raise IndexError(f"Index {index} out of range.")
            return self._items[index]
        raise TypeError(f"Indices must be integers, not {type(index).__name__}")
    
    def __contains__(self, item) -> bool:
        return item in self._items
    
    def __str__(self) -> str:
        if len(self._items) == 0:
            return "Collection is empty."
        result = f"Collection contains {len(self._items)} item(s):\n"
        result += "-" * 50 + "\n"
        for i, item in enumerate(self._items):
            result += f"[{i}] {item}\n"
        result += "-" * 50
        return result
    
    def __repr__(self) -> str:
        return f"TypedCollection(items={repr(self._items)})"