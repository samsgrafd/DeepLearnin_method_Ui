from tensorpy import image_base


image_path = "http://defenders.org/sites/default/files/styles/large/public/dolphin-kristian-sekulic-isp.jpg"

result = image_base.classify(image_path)

print("\nBest match classification:\n%s\n" % result)