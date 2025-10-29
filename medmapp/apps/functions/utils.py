



from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def compress_image(image, quality=70):
    """Compress image and return a new Django-friendly file"""
    img = Image.open(image)

    # Convert all images to RGB (some formats like PNG can cause errors)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # Save into memory buffer
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True)

    return ContentFile(buffer.getvalue())
