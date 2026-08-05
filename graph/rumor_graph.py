from langgraph.graph import StateGraph

from typing import TypedDict


class GraphState(TypedDict):

    question: str

    answer: str


def retrieve_node(state):

    print(
        "\nINFO --- [NODE] EVIDENCE RETRIEVAL ---"
    )

    return state


def reasoning_node(state):

    print(
        "\nINFO --- [NODE] LLM REASONING ---"
    )

    return state


def create_graph():

    graph = StateGraph(GraphState)

    graph.add_node(
        "retrieve",
        retrieve_node
    )

    graph.add_node(
        "reason",
        reasoning_node
    )

    graph.set_entry_point(
        "retrieve"
    )

    graph.add_edge(
        "retrieve",
        "reason"
    )

    return graph.compile()