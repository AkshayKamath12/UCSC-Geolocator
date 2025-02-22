# import os
# from PIL import Image, ExifTags
# from pillow_heif import register_heif_opener
# from datetime import datetime
# import piexif
# import re
# register_heif_opener()

# def convert_heic_to_jpeg(dir_of_interest):
#     filenames = os.listdir(dir_of_interest)
#     filenames_matched = [filename for filename in filenames]

#     # Extract files of interest
#     HEIC_files = []
#     for index, filename in enumerate(filenames_matched):
#             if filename:
#                     HEIC_files.append(filenames[index])

#     # Convert files to jpg while keeping the timestamp
#     for filename in HEIC_files:
#             image = Image.open(dir_of_interest + "/" + filename)
#             image_exif = image.getexif()
#             if image_exif:
#                     # Make a map with tag names and grab the datetime
#                     exif = { ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS and type(v) is not bytes }
#                     date = datetime.strptime(exif['DateTime'], '%Y:%m:%d %H:%M:%S')

#                     # Load exif data via piexif
#                     exif_dict = piexif.load(image.info["exif"])

#                     # Update exif data with orientation and datetime
#                     exif_dict["0th"][piexif.ImageIFD.DateTime] = date.strftime("%Y:%m:%d %H:%M:%S")
#                     exif_dict["0th"][piexif.ImageIFD.Orientation] = 1
#                     exif_bytes = piexif.dump(exif_dict)

#                     # Save image as jpeg
#                     image.save(dir_of_interest + "/" + os.path.splitext(filename)[0] + ".jpg", "jpeg", exif= exif_bytes)
#                     os.remove(dir_of_interest + "/" + filename)
#             else:
#                     print(f"Unable to get exif data for {filename}")

# convert_heic_to_jpeg("Andre's Photos-20250220T061424Z-001")


import exifread #note: need to install
import os
import random

# def get_gps_coords(image_path):
#     with open(image_path, "rb") as img_file:
#         tags = exifread.process_file(img_file)

#     # Extract GPS coordinates if available
#     gps_lat = tags.get("GPS GPSLatitude")
#     gps_lat_ref = tags.get("GPS GPSLatitudeRef")
#     gps_lon = tags.get("GPS GPSLongitude")
#     gps_lon_ref = tags.get("GPS GPSLongitudeRef")

#     if gps_lat and gps_lon:
#         lat = convert_to_degrees(gps_lat)
#         lon = convert_to_degrees(gps_lon)

#         # Adjust for hemisphere
#         if gps_lat_ref and gps_lat_ref.values[0] == "S":
#             lat = -lat
#         if gps_lon_ref and gps_lon_ref.values[0] == "W":
#             lon = -lon

#         return {"latitude": lat, "longitude": lon}
#     return None

# def convert_to_degrees(value):
#     d, m, s = [float(v.num) / float(v.den) for v in value.values]
#     return d + (m / 60.0) + (s / 3600.0)

directions = ["N", "W", "E", "S", "NE", "NW", "SE", "SW"]
for file in os.listdir("Trial 5 - 8 Trigrams v2 -"):
  args = file.split("$")
  file = f"Trial 5 - 8 Trigrams v2 -/{file}"
  print(file)
  
  print(args)
  # gps_data = get_gps_coords(file)
  os.rename(file, f"Trial 5 - 8 Trigrams v2 -/{args[1]}_{args[0]}_{args[2]}")
#   try:
#     os.rename(file, f"Trial 5 - 8 Trigrams v2 -/{gps_data['latitude']:.6f}_{gps_data['longitude']:.6f}_{random.choice(directions)}.JPEG")
#   except:
#       pass
