from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>Sample Website</title>
</head>
<body>
<h1>Welcome</h1>
<h2>Python Project</h2>
<h2>Data Scraping Example</h2>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print("Website Title:")
print(soup.title.text)

print("\nHeadings:")

for heading in soup.find_all(["h1", "h2"]):
    print(heading.text)
    
    
