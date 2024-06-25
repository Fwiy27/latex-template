import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Header):
        # Convert # headers to \chapter{}
        if elem.level == 1:
            title = pf.stringify(elem).strip()
            return pf.RawBlock(f'\\chapter{{{title}}}', format='latex')
        # Convert ## headers to \section{}
        elif elem.level == 2:
            title = pf.stringify(elem).strip()
            return pf.RawBlock(f'\\section{{{title}}}', format='latex')
        
    if isinstance(elem, pf.Para):
        # Handles Questions
        text = pf.stringify(elem)
        if text.startswith('!!! qs'):
            content = text.replace('!!! qs', '', 1).strip()
            latex_output = process_question(content)
            if latex_output:
                return pf.RawBlock(latex_output, format='latex')
        # Handles Definition
        if text.startswith('!!! def'):
            content = text.replace('!!! def', '', 1).strip()
            latex_output = process_definition(content)
            if latex_output:
                return pf.RawBlock(latex_output, format='latex')
    return elem

def process_question(content: str):
    # Implement your custom logic here to process the content
    # For example:
    
    title = content[:content.find('|')].strip()
    info = content[content.find('|')+1:].strip()
    
    return f'\\qs{'{'}{title}{'}'}{'{'}{info}{'}'}'

def process_definition(content: str):
    # Implement your custom logic here to process the content
    # For example:
    
    title = content[:content.find('|')].strip()
    info = content[content.find('|')+1:].strip()
    
    return f'\\dfn{'{'}{title}{'}'}{'{'}{info}{'}'}'

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
