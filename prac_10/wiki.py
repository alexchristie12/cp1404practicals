"""
CP1404 Practical 10: Wikipedia API
Estimated Time: 30 minutes
Actual Time: 40 minutes
"""
import wikipedia as wiki


def main():
    """Main program body for wikipedia exercise."""
    search_prompt = input("\nEnter a page title or search phrase: ")
    while search_prompt != "":
        search_results = wiki.search(search_prompt)
        search_result = handle_search_results(search_results)
        try:
            wiki_page = wiki.page(search_result, auto_suggest=False)
        except wiki.DisambiguationError as disambiguation_options:
            print("You have selected a Disambiguation, select the one that you really want")
            search_result = handle_search_results(disambiguation_options.options)
            wiki_page = wiki.page(search_result, auto_suggest=False)
        print(wiki_page.title)
        print(wiki_page.summary)  # I don't like how it is all one line
        print(wiki_page.url)

        search_prompt = input("Enter a page title or search phrase: ")


def handle_search_results(search_results: list) -> str:
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
