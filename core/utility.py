from PIL import Image
import os
from django.conf import settings


def create_thumbnail(image_field, size=(300, 300)):
    """
    Generates a thumbnail for an image field and saves it alongside the original image.

    Args:
        image_field: The ImageField instance to generate a thumbnail for.
        size (tuple): Thumbnail size in (width, height).

    Returns:
        str: The path of the generated thumbnail relative to MEDIA_ROOT.
    """
    if not image_field or not image_field.name:
        return None

    # Determine the original image path
    image_path = os.path.join(settings.MEDIA_ROOT, image_field.name)

    # Verify the file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Open and process the image
    with Image.open(image_path) as img:
        # Convert to RGB if needed
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Create the thumbnail
        img.thumbnail(size)

        # Save the thumbnail
        base, ext = os.path.splitext(image_field.name)
        thumbnail_name = f"{base}_thumbnail{ext}"
        thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail_name)
        img.save(thumbnail_path, "JPEG")

    return thumbnail_name