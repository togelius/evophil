"""
Evophil - Evolving Philosophy

A module for evolving philosophical concepts using evolutionary algorithms.
"""

from typing import List


class Population:
    """A population of philosophical concepts represented as strings."""

    def __init__(self):
        """Initialize an empty population."""
        self._individuals: List[str] = []

    @property
    def individuals(self) -> List[str]:
        """Return the list of individuals in the population."""
        return self._individuals

    @property
    def size(self) -> int:
        """Return the number of individuals in the population."""
        return len(self._individuals)

    def is_empty(self) -> bool:
        """Check if the population is empty."""
        return len(self._individuals) == 0


def create_population() -> Population:
    """Create and return an empty population."""
    return Population()


if __name__ == "__main__":
    population = create_population()
    print(f"Created population with {population.size} individuals")
    print(f"Population is empty: {population.is_empty()}")
