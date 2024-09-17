import logging
from PIL import Image
from .enums import AspectRatio

__all__ = ["crop_image"]

LOG = logging.getLogger(__name__)


def crop_image(src_path: str, dst_path: str, aspect_ratio: AspectRatio):
    LOG.info(f"Starting image crop process for {src_path}")
    try:
        image = Image.open(src_path)
        LOG.debug(f"Image opened successfully: {src_path}")

        width, height = image.size
        LOG.info(f"Original image dimensions: {width}x{height}")

        ratio = aspect_ratio.value["ratio"]
        LOG.debug(f"Target aspect ratio: {ratio}")

        new_width, new_height = closest_resolution_by_height(height, ratio)
        LOG.info(f"New dimensions after cropping: {new_width}x{new_height}")

        remainder = width - new_width
        half_remainder = remainder / 2

        left = half_remainder
        right = width - half_remainder
        top = 0
        bottom = new_height

        LOG.debug(
            f"Crop coordinates: left={left}, top={top}, right={right}, bottom={bottom}"
        )

        image_cropped = image.crop((left, top, right, bottom))
        image_cropped.save(dst_path)
        LOG.info(f"Cropped image saved successfully: {dst_path}")

    except IOError as e:
        LOG.error(f"Error opening or saving image: {e}")
    except Exception as e:
        LOG.error(f"Unexpected error during image cropping: {e}")


def closest_resolution_by_height(height: int, aspect_ratio: str):
    LOG.debug(
        f"Calculating closest resolution for height {height} and aspect ratio {aspect_ratio}"
    )
    aspect_width, aspect_height = map(int, aspect_ratio.split(":"))
    aspect_ratio = aspect_width / aspect_height
    new_width = int(height * aspect_ratio)
    LOG.debug(f"Calculated dimensions: {new_width}x{height}")
    return new_width, height
