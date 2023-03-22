from jinja2 import Template
#Template is a class in jinja2

TEMPLATE = """ Hello {{ name }} ! """
# variables are given inside {{var_name}} in jinja2

def main():
    template = Template(TEMPLATE)
    print(template.render(name = "Ram")) # templates must be rendered in jinja2
    
if __name__== "__main__":
    main()
