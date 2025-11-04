import synalinks
from typing import List, Optional

class ScientificQuery(synalinks.DataModel):
    """
    Scientific question input model.

    This model represents a scientific query with an optional domain specification
    and contextual information to help generate more accurate and relevant answers.

    Attributes:
        question: The scientific question to be answered
        domain: Optional scientific domain (e.g., physics, biology, chemistry)
        context: Optional additional context for the question
    """
    question: str = synalinks.Field(
        description="The scientific question to be answered"
    )
    domain: Optional[str] = synalinks.Field(
        description="Scientific domain (e.g., physics, biology, chemistry)",
        default=None
    )
    context: Optional[str] = synalinks.Field(
        description="Additional context for the question",
        default=None
    )

class Citation(synalinks.DataModel):
    """
    Citation for scientific sources.

    This model represents a bibliographic citation with all necessary metadata
    for referencing scientific sources including papers, books, and online resources.

    Attributes:
        title: Title of the source
        authors: List of author names
        year: Optional publication year
        source: Source type or name (journal, book, website, etc.)
        url: Optional URL to access the source
    """
    title: str = synalinks.Field(
        description="Title of the source"
    )
    authors: List[str] = synalinks.Field(
        description="List of authors"
    )
    year: Optional[int] = synalinks.Field(
        description="Publication year",
        default=None
    )
    source: str = synalinks.Field(
        description="Source (journal, book, website, etc.)"
    )
    url: Optional[str] = synalinks.Field(
        description="URL if available",
        default=None
    )

class ScientificAnswer(synalinks.DataModel):
    """
    Comprehensive scientific answer model.

    This model represents a complete scientific answer with background context,
    reasoning, citations, and recommendations for further reading. It provides
    a structured format for presenting scientific information with proper attribution.

    Attributes:
        background: Background information and context for the question
        reasoning: Step-by-step reasoning process and explanation
        answer: Clear and concise answer to the question
        confidence: Confidence score between 0 and 1 indicating answer reliability
        citations: List of scientific citations supporting the answer
        further_reading: Optional list of recommended resources for deeper understanding
    """
    background: str = synalinks.Field(
        description="Background information and context for the question"
    )
    reasoning: str = synalinks.Field(
        description="Step-by-step reasoning process and explanation"
    )
    answer: str = synalinks.Field(
        description="Clear and concise answer to the question"
    )
    confidence: float = synalinks.Field(
        description="Confidence score between 0 and 1",
        default=0.0
    )
    citations: List[Citation] = synalinks.Field(
        description="Scientific citations supporting the answer"
    )
    further_reading: Optional[List[str]] = synalinks.Field(
        description="Suggested further reading on the topic",
        default=None
    ) 