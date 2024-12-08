from scripts.data_preprocessing import preprocess
from scripts.data_analysis import analyze_data
from scripts.model_training import train_model
from scripts.api_integration import fetch_real_time_data
from scripts.gui import launch_gui
if __name__ == "__main__":
    # Step 1: Data Preprocessing
    data = preprocess()

    # Step 2: Data Analysis
    analyze_data(data)

    # Step 3: Train Model
    model = train_model(data)

    # Step 4: Fetch Real-time Data
    real_time_data = fetch_real_time_data()

    # Step 5: Launch GUI
    launch_gui(model)