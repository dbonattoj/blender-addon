import imageio
import os

def convert(filename):
  filename_wo_ext = filename.split(".")[0]

  image = imageio.imread(filename)
  
  print(f"Converting {filename} of shape {image.shape}.")
  
  out = image/image.max()
  out = out * 255
  
  imageio.imwrite(filename_wo_ext + ".png", out.astype('uint8'))
  

if __name__ == "__main__":
  for file in os.listdir("."):
    if file.endswith(".pfm"):
      convert(file)
