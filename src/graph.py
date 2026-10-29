from langgraph.graph import StateGraph, START, END

from src.nodes import edited_text_node, summarizer_node
from src.state import SummarizerState


def build_graph():
    graph = StateGraph(SummarizerState)

    graph.add_node("edit_node", edited_text_node)
    graph.add_node("summary_node", summarizer_node)

    graph.add_edge(START, "edit_node")
    graph.add_edge("edit_node", "summary_node")
    graph.add_edge("summary_node", END)

    return graph.compile()

app = build_graph()