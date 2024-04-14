from psmoe import predictor
import os



# First download the models if not already downloaded
predictor.model_downloader()

# Second load the models
nets = predictor.model_loading()

# You can download an example if needed
predictor.load_example()

# Third predict the subject
results = predictor.predict(os.path.join("test_images","sujeto_006.nii"),nets)
print(f"Volumen prostático = {results['volume']} ml")

# Alternative to predict and plot middle image in sequence
#predictor.seg_plot(os.path.join("test_images","sujeto_006.nii"),nets)