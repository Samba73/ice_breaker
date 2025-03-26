from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url(name: str):
    """Searches for LinkedIn or Twitter Profile Page."""

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res