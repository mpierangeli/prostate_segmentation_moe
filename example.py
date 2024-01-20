import predictor


if __name__ == "__main__":
    
    # First download the models if not already downloaded
    predictor.model_downloader()
    
    # Second load the models
    nets = predictor.model_loading()
    
    # Third predict the subject
    results = predictor.predict("test_images\sujeto_006.nii",nets)
    
    # Alternative to predict and plot middle image in sequence
    #predictor.seg_plot("test_images\sujeto_006.nii",nets)