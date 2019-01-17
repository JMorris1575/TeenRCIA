from activity.models import ImageQuote

import random, os

def get_quote_image():
    image_quote = random.choice(ImageQuote.objects.all())
    return os.path.join('activity', 'images', image_quote.image_filename)