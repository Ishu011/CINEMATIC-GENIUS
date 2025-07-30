# CINEMATIC GENIUS : Movie Recommender system
## a) Overview

**Cinematic-Genius-Movie-Recommender-System** is an advanced movie recommender system that harnesses the power of collaborative filtering and content-based filtering techniques to offer personalized movie suggestions. This application not only helps users discover new movies but also provides detailed information on each recommendation, including title, release date, rating, main characters, and posters. The system is powered by cutting-edge machine learning algorithms and integrates seamlessly with The Movie Database (TMDb) API for fetching up-to-date movie details.

In addition to its robust recommendation capabilities, Cinematic Genius includes extensive customization features, allowing users to personalize the application's appearance to match their preferences. With options to adjust background colors, text colors, fonts, and overall style, users can create a viewing experience that feels uniquely theirs.

## DEMO LINK : https://drive.google.com/file/d/10f8aYUoAyJuYis-icAcGA5iern9BuI6s/view?usp=sharing

## b) Features

- **Movie Search**: An intuitive search bar that allows users to find movies by title quickly.
- **Hybrid Recommendation Algorithms**: Combines collaborative filtering and content-based filtering to generate highly accurate and personalized movie recommendations.
- **Detailed Movie Information**: Provides comprehensive details on recommended movies, such as title, release date, rating, main characters, overview, and movie posters.
- **Responsive UI**: A user-friendly interface built with Streamlit, enabling easy interaction and exploration of movie recommendations.

- 
- **c) Appearance Customization**
- 
  - **Background Color**: Users can change the primary and secondary background colors to suit their preferences.
  - **Text Color**: Customizable text color for better readability or aesthetic appeal.
  - **Style and Font**: Options to select different styles and fonts, allowing users to personalize the look and feel of the application.
  - **Mode Features**: Includes a toggle for switching between different modes (e.g., Light Mode, Dark Mode) for varied visual experiences.
  - **Appearance Settings**: Accessible settings button to manage all appearance-related features in one place.
 
  - ![Screenshot 2024-08-30 021543](https://github.com/user-attachments/assets/3ae8317d-5480-4c53-b798-58e7011c0cb2)
  - ![Screenshot 2024-08-30 021652](https://github.com/user-attachments/assets/4a6dd1ba-8a7f-4213-aeb1-19d279bac497)




## d) Technologies Used

- **Streamlit**: For creating an interactive web application with a dynamic and responsive user interface.
- **Pandas**: For efficient data manipulation and analysis.
- **Scikit-learn**: For implementing machine learning algorithms such as Truncated SVD and cosine similarity.
- **Requests**: For making API requests to The Movie Database (TMDb) to retrieve additional movie details.
- **Pickle**: For loading preprocessed movie data to enhance performance.
- **TMDb API**: For fetching movie metadata including posters, ratings, and summaries.


## e) Installation

To set up the project locally, follow these steps:

### 1. Clone the Repository

git clone https://github.com/Ishu/Cinematic-Genius-Movie-Recommender-System.git
cd Cinematic-Genius-Movie-Recommender-System

### 2.Set Up a Virtual Environment (Optional but Recommended)

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install Required Packages**

   pip install -r requirements.txt

   ### 3. Install Required Packages
   
pip install -r requirements.txt

### 4. Obtain TMDb API Key

Sign up at The Movie Database and get your API key.
Replace the placeholder API key in the code with your own key.

### 5. Prepare Data

Place your movies_metadata.csv, ratings_small.csv, and keywords.csv files in the project directory.

### 6. Run the Application

streamlit run app.py

### f) Search for a Movie
- Enter the movie title in the search bar and select a movie from the dropdown list.

### g) Get Recommendations
- Choose the recommendation type (collaborative or content-based).
- Select the number of recommendations you want to receive.
- Click the "Recommend" button to view a list of personalized movie suggestions.

### h) View Movie Details
- For each recommended movie, view detailed information including the poster, title, release date, rating, main characters, and an overview.

### i) Customize Appearance
- Click the **Settings** button to access appearance customization options.
- Adjust the background color, text color, style, and font.
- Toggle between Light Mode and Dark Mode for a preferred visual experience.

## j) File Structure
- **`app.py`**: The main Streamlit application script.
- **`movies_metadata.csv`**: Metadata file containing movie details.
- **`ratings_small.csv`**: Ratings data used for generating recommendations.
- **`keywords.csv`**: Keywords data used for content-based filtering.
- **`requirements.txt`**: File listing the project dependencies.
- **`movie_dict_with_titles.pkl`**: Pickled file containing processed movie data for fast loading.

## k) Example Output

![Screenshot 2024-08-30 021055](https://github.com/user-attachments/assets/2df36556-c567-4cd7-9b52-aa111349e162)


_A screenshot of the application showcasing movie recommendations, detailed movie information, and the customization settings panel._

## l) Contributing

Contributions to the project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## m) License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Ishu**

---------------------**THANKYOU**



