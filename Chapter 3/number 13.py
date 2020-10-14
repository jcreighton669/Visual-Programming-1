rowLength = int(input("Enter the length of the row in feet: "))
endPost = int(input("Enter the space for the end-post assembly: "))
spaceBetween = int(input("Enter the space between the vines: "))

grapevines = (rowLength - (2 * endPost)) // spaceBetween

print("This will yield {} grapevines.".format(grapevines))
