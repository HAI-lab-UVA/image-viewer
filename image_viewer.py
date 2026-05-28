import os
import sys
from pathlib import Path
import re

class ImageViewer():
    __images = []

    def add_images_from_directory(self, directory : str):
        self.__images.extend(self.__get_valid_images_from_dir(directory))
    
    def add_image(self, image_path : str):
        if self.__validate_image(image_path):
            self.__images.append(image_path)

    def sort_images(self, descending : bool = False):
        """
        Sorts images alphabetically (A-Z) according to their filenames. If descending, sorts Z-A.
        """
        if descending:
            self.__images.sort(reverse = True)
        else:
            self.__images.sort()

    def sort_images_by_regex(self, patterns : list[str], 
                             descending : bool = False,
                             remove_unmatched_images : bool = False):
        """
        Sorts images according to a list of regex patterns. 
        Image filenames matching the first pattern are sorted first (if descending, they are sorted last).
        Image filenames matching no patterns are sorted last without modifying their original order (if descending, they are sorted first).
        If `remove_unmatched_images` is true, image filenames matching no patterns are removed.
        """

        self.__images = self.__regex_sort(self.__images, patterns, remove_unmatched_images)

        if descending:
            self.__images.reverse()
 
    def remove_image(self, image_name : str):
        if image_name in self.__images:
            self.__images.remove(image_name)
        else:
            print(f"{image_name} was not found.", file=sys.stderr)

    def remove_all_images(self):
        self.__images = []

    def render_html(self, output_file : str):
        with open('image_viewer_template.html', 'r') as f:
            filedata = f.read()
            filedata = filedata.replace(
                    "IMAGE_FILES",
                    ",".join([f"\"{x}\"" for x in self.__images])
                    )
            
            abs_paths = [f"\"{Path(x).resolve().as_posix()}\"" for x in self.__images]
            abs_paths = [x.replace("/", "//") for x in abs_paths]
            print(abs_paths)
            filedata = filedata.replace(
                    "ABS_PATHS",
                    ",".join(abs_paths)
                    )
            output = Path(output_file).resolve().with_suffix(".html")
        
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, 'w') as f:
            f.write(filedata)
        
        print(f"HTML file saved to {output}")

    def __get_valid_images_from_dir(self, directory) -> list[str]:
        try:
            images = os.listdir(directory)
            if len(images) == 0:
                raise Exception(f"Directory {directory} is empty.")
        except Exception as e:
            print(e)

        valid_images = []
        for i in images:
            if self.__validate_image(i):
                valid_images.append(os.path.join(directory, i))
        return valid_images

    def __validate_image(self, image: str) -> bool:
        if (image.endswith(".png") 
            or image.endswith(".jpg") 
            or image.endswith(".jpeg") 
            ):
            return True
        else:
            print(f"File {image} is not a valid image (must be PNG, JPG, or JPEG).", file=sys.stderr)
            return False

    def __regex_sort(self, images : list[str], 
                     patterns : list[str], 
                     remove_unmatched_images : bool):
        sorted = []
        unsorted = images
        for pattern in patterns:
            matches = [x for x in unsorted if re.search(pattern , x)]
            for m in matches:
                unsorted.remove(m)
            sorted.extend(matches)

        if not remove_unmatched_images and len(unsorted) > 0:
            sorted.extend(unsorted)

        return sorted
    
    @property
    def images(self):
        return self.__images
    
        
    
    
                
