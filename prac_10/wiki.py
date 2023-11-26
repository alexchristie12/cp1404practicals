"""
CP1404 Practical 10: Wikipedia API
Estimated Time: 30 minutes
Actual Time:
"""
import wikipedia as wiki


def main():
    """Main program body for wikipedia exercise."""
    search_prompt = input("Enter a page title or search phrase: ")
    results = wiki.search(search_prompt)
    result = handle_search_prompts(results)
    wiki_page = wiki.page(result, auto_suggest=False)
    print(wiki_page.title)
    print(wiki_page.summary)  # I don't like how it is all one line
    print(wiki_page.url)


def handle_search_prompts(search_results: list) -> str:
    """Takes in a list of results from the wikipedia API and prompts the user to select an input"""
    selected_result = ""
    valid_selection = False
    if len(search_results) == 0:
        valid_selection = True  # There is no result that the user can select
    else:
        for i, search_result in enumerate(search_results):
            print(f"{i}. {search_result}")
    while not valid_selection:
        try:
            selection_index = int(input("Enter a number corresponding to the desired search result: "))
            selected_result = search_results[selection_index]
            valid_selection = True
        except ValueError:
            print("Invalid Input")
        except IndexError:
            print("Invalid Index")
    return selected_result


main()
