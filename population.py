"""
Evophil - Evolving Philosophy

A module for evolving philosophical concepts using evolutionary algorithms.
"""

from typing import List, Optional

import anthropic


DEFAULT_PROMPT = """Please create five different definitions of knowledge. Each definition should be between 2 and 20 words long. Write each definition on a new line, and include nothing else in your response."""


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

    def initialize_from_llm(self, prompt: Optional[str] = None) -> None:
        """Initialize the population by querying an LLM.

        Args:
            prompt: The prompt to send to the LLM. If None, uses DEFAULT_PROMPT.
        """
        if prompt is None:
            prompt = DEFAULT_PROMPT

        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = message.content[0].text
        lines = [line.strip() for line in response_text.strip().split("\n") if line.strip()]
        self._individuals = lines


def create_population() -> Population:
    """Create and return an empty population."""
    return Population()


if __name__ == "__main__":
    population = create_population()
    print(f"Created empty population with {population.size} individuals")
    print(f"Population is empty: {population.is_empty()}")

    print("\nInitializing population...")
    population._individuals = [
        "Knowledge is a belief that is both true and supported by sufficient evidence.",
        "Knowledge is a true belief caused directly by the fact being believed.",
        "Knowledge is a true belief produced by a consistently dependable cognitive process.",
        "Knowledge is a successful belief arising from the agent's intellectual excellence or character.",
        "Knowledge is a fundamental, unanalyzable mental state rather than a composite of parts.",
    ]
    print(f"Population now has {population.size} individuals:")
    for i, individual in enumerate(population.individuals, 1):
        print(f"  {i}. {individual}")
