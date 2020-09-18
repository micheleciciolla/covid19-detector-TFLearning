import Augmentor

p = Augmentor.Pipeline("dataset/train/covid")
# Point to a directory containing ground truth data.
# Images with the same file names will be added as ground truth data
# and augmented in parallel to the original data.

# Add operations to the pipeline as normal:
p.rotate(probability=0.7, max_left_rotation=5, max_right_rotation=5)
howmany = 84
p.sample(howmany)
p.flip_left_right(probability=0.5)
p.sample(howmany)
p.zoom_random(probability=0.3, percentage_area=0.8)
p.sample(howmany)
p.random_distorsion(probability=0.3)
p.sample(30)
p.skew(probability=0.3)
p.sample(30)
