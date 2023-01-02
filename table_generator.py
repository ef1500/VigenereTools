import sys
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

def print_vigenere_table(alpha1, alpha2, image=False):
  # Check that the alphabets are the same size
  if len(alpha1) != len(alpha2):
    raise ValueError("Alphabets must be the same size")
  n = len(alpha1)
  
  # Print the top row of the table
  print("  ", end="")
  for i in range(n):
    print(f"{alpha1[i]} ", end="")
  print()
  
  # Print the rest of the table
  for i in range(n):
    print(f"{alpha2[i]} ", end="")
    for j in range(n):
      print(f"{alpha2[(j+i) % n]} ", end="")
    print()
    
    if image:
        # Create an image with a white background
        image = PIL.Image.new("RGB", (n*50 + 10, n*50 + 10), (255, 255, 255))
        draw = PIL.ImageDraw.Draw(image)
        font = PIL.ImageFont.truetype("arial.ttf", 20)

        # Draw the top row of the table
        draw.text((5, 5), "  ", font=font, fill=(0, 0, 0))
        for i in range(n):
            draw.text((50*i + 35, 5), f"{alpha1[i]} ", font=font, fill=(0, 0, 0))

        # Draw the rest of the table
        for i in range(n):
            draw.text((5, 50*i + 35), f"{alpha2[i]} ", font=font, fill=(0, 0, 0))
            for j in range(n):
                draw.text((50*j + 35, 50*i + 35), f"{alpha2[(j+i) % n]} ", font=font, fill=(0, 0, 0))

        # Save the image
        image.save("vigenere_table.jpg")

    
alphabet = sys.argv[1]
try:
    image = sys.argv[2]
except:
    image = False
print_vigenere_table(alphabet, alphabet, image)