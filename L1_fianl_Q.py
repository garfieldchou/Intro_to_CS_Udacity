# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
# print page
start_link = page.find('<a href=')
first_quote = page.find('"', start_link)
second_quote = page.find('"', first_quote+1) # start with 'first_quote+1' instead of 'first_quote'
url = page[first_quote+1 : second_quote]
print url