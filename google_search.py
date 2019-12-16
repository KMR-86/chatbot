from serpwow.google_search_results import GoogleSearchResults
import json
api_key="753B09F4DDAE455B81E8ABB736C8033A"
# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults(api_key)
j=0
while j in range(0,5):
    user_input=input("Google: ask me anything\n")
    # set up a dict for the search parameters
    params = {
    "q" : user_input
    }

    # retrieve the search results as JSON
    result = serpwow.get_json(params)

    # pretty-print the result
    returned_text=json.dumps(result, indent=2, sort_keys=True)
    #print(returned_text)
    #print(len(returned_text))
    index=returned_text.find("knowledge_graph")
    if index==-1:
        print("sorry, couldnt find the result. try something else\n")
        continue
    
    info=returned_text[index:index+1000]
    index2=info.find("description")
    search_result=""
    #print(len(info))
    for i in range(index2+15,index2+500):
        search_result=search_result+info[i]
        if info[i]=="\n":
            #print("\nfound newline\n")
            break

    print("Google: \n",search_result)
