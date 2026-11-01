import streamlit as st

from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

st.set_page_config(page_title="Multi-Agent Research", page_icon="🔎", layout="wide")

# ---------- Sidebar ----------
with st.sidebar:
    st.title("🔎 Multi-Agent Research")
    st.caption("Search → Read → Write → Critique")
    st.markdown(
        """
**Pipeline**
1. 🔍 Search Agent finds sources
2. 📖 Reader Agent scrapes the best page
3. ✍️ Writer drafts the report
4. 🧐 Critic reviews the report
"""
    )
    if st.button("Clear results", use_container_width=True):
        st.session_state.pop("state", None)
        st.session_state.pop("topic", None)
        st.rerun()

# ---------- Header ----------
st.title("Multi-Agent Research System")
st.write("Enter a topic and a team of AI agents will research it and write a report.")

SUGGESTIONS = [
    "Latest advances in quantum computing",
    "Impact of AI on healthcare",
    "Future of renewable energy storage",
]

if "topic_input" not in st.session_state:
    st.session_state.topic_input = ""

cols = st.columns(len(SUGGESTIONS))
for col, suggestion in zip(cols, SUGGESTIONS):
    if col.button(suggestion, use_container_width=True):
        st.session_state.topic_input = suggestion

with st.form("research_form", clear_on_submit=False):
    topic = st.text_input(
        "Research topic",
        key="topic_input",
        placeholder="e.g. Latest advances in quantum computing",
    )
    submitted = st.form_submit_button("🚀 Start Research", type="primary")


# ---------- Pipeline (with live progress) ----------
def run_with_progress(topic: str) -> dict:
    state = {}

    with st.status("Step 1 · Search agent is working...", expanded=True) as status:
        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
        })
        state["search_results"] = search_result["messages"][-1].content
        status.update(label="Step 1 · Search complete ✅", state="complete", expanded=False)

    with st.status("Step 2 · Reader agent is scraping top resources...", expanded=True) as status:
        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}"
            )]
        })
        state["scraped_content"] = reader_result["messages"][-1].content
        status.update(label="Step 2 · Scraping complete ✅", state="complete", expanded=False)

    with st.status("Step 3 · Writer is drafting the report...", expanded=True) as status:
        research_combined = (
            f"SEARCH RESULTS : \n {state['search_results']} \n\n"
            f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
        )
        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined,
        })
        status.update(label="Step 3 · Report drafted ✅", state="complete", expanded=False)

    with st.status("Step 4 · Critic is reviewing the report...", expanded=True) as status:
        state["feedback"] = critic_chain.invoke({"report": state["report"]})
        status.update(label="Step 4 · Review complete ✅", state="complete", expanded=False)

    return state


if submitted:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        try:
            st.session_state.state = run_with_progress(topic.strip())
            st.session_state.topic = topic.strip()
        except Exception as e:
            st.error(f"Something went wrong: {e}")


# ---------- Results ----------
state = st.session_state.get("state")
if state:
    st.divider()
    st.subheader(f"Results: {st.session_state.get('topic', '')}")

    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["📄 Final Report", "🧐 Critic Feedback", "🔍 Search Results", "📖 Scraped Content"]
    )

    with tab_report:
        st.markdown(state["report"])
        st.download_button(
            "⬇️ Download report (.md)",
            data=state["report"],
            file_name="research_report.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.markdown(state["feedback"])
        st.download_button(
            "⬇️ Download feedback (.md)",
            data=state["feedback"],
            file_name="critic_feedback.md",
            mime="text/markdown",
        )

    with tab_search:
        st.markdown(state["search_results"])

    with tab_scraped:
        st.markdown(state["scraped_content"])