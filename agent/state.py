from dataclasses import dataclass, field


@dataclass
class AgentState:

    query: str

    storage_summary: dict = field(
        default_factory=dict
    )

    forecast: dict = field(
        default_factory=dict
    )

    recommendations: list = field(
        default_factory=list
    )

    tool_results: dict = field(
        default_factory=dict
    )

    response: str = ""