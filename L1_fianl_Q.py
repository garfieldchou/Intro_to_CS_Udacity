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
# print 'start_link= ', start_link
# print 'after start_link= ', page[start_link:]
first_quote = page.find('"', start_link)
# print 'first quote= ', first_quote
# print 'after first_quote= ', page[first_quote:]
second_quote = page.find('"', first_quote+1)
# print 'second quote= ', second_quote
# print 'after second_quote= ', page[second_quote:]
url = page[first_quote+1 : second_quote]
print url