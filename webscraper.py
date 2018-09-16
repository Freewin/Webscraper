from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src="http://source.unsplash.com/200x200/?nature,water">
        <p>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
        eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut porttitor leo a diam sollicitudin tempor id eu nisl.
         Scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt.
        </p>
    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 1</a></li>
        </ul>
    </div>
</body>
</html>        
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct Calls
print(soup.body)
print(soup.head)
print(soup.head.title)

# find()
el1 = soup.find('div')
print(el1)

# find_all()
el2 = soup.find_all('div')
el3 = soup.find_all('div')[1]
print(el2, el3)

el4 = soup.find(id='section-1')
el5 = soup.find(class_='items')
el6 = soup.find(attrs={"data-hello": "h1"})
print(el4, el5, el6)

# select
el7 = soup.select('#section-1')
el8 = soup.select('#section-1')[0]
el9 = soup.select('.item')[0]
print(el7, el8, el9)

#get_text()
el10 = soup.find(class_='item').get_text()
print(el10)

for item in soup.select('.item'):
    print(item.get_text())


el11 = soup.body.contents[1].contents[1].next_sibling.next_sibling
el12 = soup.body.contents[1].contents[1].find_next_sibling()
el13 = soup.find(id='section-2').find_previous_sibling()
el14 = soup.find(class_='item').find_parent()
el15 = soup.find('h3').find_next_sibling('p')

print(el11, el12, el13, el14, el15)
