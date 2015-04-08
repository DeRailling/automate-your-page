def generate_concept_HTML(concept_title, concept_description):
    #This procedure takes in text arguments concept title and concept description
    #and generates nested div html code based of those arguments

    div_concept_title = '''
    <div class="concept">
        <div class="concept-title">
              ''' + concept_title
    div_concept_descr = '''
        </div>
        <div class="concept-description">
              ''' +  concept_description
    div_closing = '''
        </div>
    </div>'''
    full_html_text = div_concept_title + div_concept_descr + div_closing
    return full_html_text


def make_HTML(concept):
    #This procedure takes in a list containing title and description elements
    #and outputs nested div of those elements in that list data structure

    concept_title = concept[0]                  #holds the first element of the list in the variable
    concept_description = concept[1]   #holds the second element of the list in the variable
    return generate_concept_HTML(concept_title, concept_description)

#This is the same sample data used in class
EXAMPLE_LIST_OF_CONCEPTS = [['Python', 'Python is a Programming Language'],
                         ['For Loop', 'For Loops allow you to iterate over lists'],
                         ['Lists', 'Lists are sequences of data']]

def make_HTML_for_many_concepts(list_of_concepts):
    #This procedure takes in a list of lists which every list contains concept title and concept description
    #and outputs nested divs as the html code for each element included in the list of concepts data structure

    #initialized  variables
    full_html_text=''
    concept_HTML =''

    #loop through list of concepts passed into procedure
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)            #call up function make_HTML  passing in
        full_html_text = full_html_text + concept_HTML   #concatenate every concept defined in the list of concepts and stored in the local variable
    return full_html_text                                              #return the contents of the local variable which should display all concepts

#use the built-in command print to print the output of the procedure make_HTML_for_many_concepts
print (make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS))
