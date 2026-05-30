from duckduckgo_search import DDGS

def emergency_support_tool(query):

    refined_query = (
        f"{query} India emergency "
        f"hospital police ambulance"
    )

    results = []


    with DDGS() as ddgs:

        search_results = ddgs.text(

            refined_query,

            max_results=5
        )


        for result in search_results:

            results.append({

                "title":
                    result["title"],

                "body":
                    result["body"]
            })


    return results