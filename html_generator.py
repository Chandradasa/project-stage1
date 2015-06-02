def add_html( concept_title, concept_description):
    html_1 = '''
      <div class = "row">
          <div class= "col-6">
              <div class=" title">  
                ''' + concept_title
                 
               
    html_2= '''
              </div> 
                 <div class= " description">  
                    ''' + concept_description
                
    html_3='''  
                </div>
           </div>
       </div>       '''
    
    
    html_total = html_1 + html_2 + html_3
    
    return html_total


def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return add_html(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
