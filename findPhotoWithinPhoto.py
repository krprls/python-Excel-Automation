import cv2

if cv2.__version__[:1] == '2':
	from cv2 import cv
	method = cv.CV_TM_SQDIFF_NORMED
elif cv2.__version__[:1] == '3':
	import cv2 as cv
	method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv.imread('small_image.png')
large_image = cv.imread('large_image.png')

result = cv.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv.imshow('output',large_image)

# The image is only displayed if we call this
cv.waitKey(0)
