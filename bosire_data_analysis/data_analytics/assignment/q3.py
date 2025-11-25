# S13/04402/21 - SETH OMONDI OTIENO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
try:
    df = pd.read_csv('imdb_movies.csv')
    print(f"Loaded {df.shape[0]:,} rows, {df.shape[1]} columns")
except FileNotFoundError:
    try:
        df = pd.read_csv('movies.csv')
        print(f"Loaded {df.shape[0]:,} rows, {df.shape[1]} columns")
    except FileNotFoundError:
        try:
            df = pd.read_csv('imdb.csv')
            print(f"Loaded {df.shape[0]:,} rows, {df.shape[1]} columns")
        except FileNotFoundError:
            print("Could not find IMDb dataset file")
            raise

print("\nFirst look at the data:")
print(df.head(5))
print(f"\nColumns: {df.columns.tolist()}")

# Prepare data for analysis
movies_df = df.copy()
movies_df.columns = movies_df.columns.str.lower().str.replace(' ', '_')

print("\nStandardized columns:")
print(movies_df.columns.tolist())

# Identify relevant columns for analysis
rating_cols = [col for col in movies_df.columns if any(word in col for word in ['rating', 'score', 'average'])]
genre_cols = [col for col in movies_df.columns if 'genre' in col]
year_cols = [col for col in movies_df.columns if any(word in col for word in ['year', 'date'])]
title_cols = [col for col in movies_df.columns if any(word in col for word in ['title', 'name', 'movie'])]

main_rating = rating_cols[0] if rating_cols else None
main_genre = genre_cols[0] if genre_cols else None
main_year = year_cols[0] if year_cols else None
main_title = title_cols[0] if title_cols else None

print(f"\nMain columns selected:")
print(f"Rating: {main_rating}, Genre: {main_genre}, Year: {main_year}, Title: {main_title}")

# Text cleaning functions
def clean_text(text):
    if pd.isna(text):
        return text
    text = str(text)
    text = re.sub(r'[^\w\s\-\.\,]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def get_year_from_title(title):
    if pd.isna(title):
        return None
    match = re.search(r'\((\d{4})\)', str(title))
    return int(match.group(1)) if match else None

def parse_genres(genre_str):
    if pd.isna(genre_str):
        return []
    genres = re.split(r'[,\|\-]', str(genre_str))
    return [g.strip().title() for g in genres if g.strip()]

# Apply data cleaning
print("\nCleaning data...")

if main_title:
    movies_df['clean_title'] = movies_df[main_title].apply(clean_text)

if main_genre:
    movies_df['clean_genres'] = movies_df[main_genre].apply(parse_genres)

if main_year:
    if movies_df[main_year].dtype == 'object':
        movies_df['release_year'] = pd.to_numeric(movies_df[main_year], errors='coerce')
    else:
        movies_df['release_year'] = movies_df[main_year]
elif main_title:
    movies_df['release_year'] = movies_df[main_title].apply(get_year_from_title)

if main_rating:
    movies_df['numeric_rating'] = pd.to_numeric(movies_df[main_rating], errors='coerce')

# Check data quality
print(f"\nDataset overview:")
print(f"Total entries: {len(movies_df):,}")

if 'release_year' in movies_df.columns:
    years = movies_df['release_year'].dropna()
    if len(years) > 0:
        print(f"Years: {years.min():.0f} to {years.max():.0f}")

if 'numeric_rating' in movies_df.columns:
    ratings = movies_df['numeric_rating'].dropna()
    if len(ratings) > 0:
        print(f"Ratings: {ratings.mean():.2f} avg, {ratings.min():.1f}-{ratings.max():.1f} range")

if 'clean_genres' in movies_df.columns:
    all_genres = [g for sublist in movies_df['clean_genres'].dropna() for g in sublist]
    print(f"Unique genres: {len(set(all_genres))}")

# Create visualizations
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Rating distribution
if 'numeric_rating' in movies_df.columns:
    ratings = movies_df['numeric_rating'].dropna()
    if len(ratings) > 0:
        axes[0,0].hist(ratings, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        axes[0,0].axvline(ratings.mean(), color='red', linestyle='--', label=f'Avg: {ratings.mean():.2f}')
        axes[0,0].legend()
    else:
        axes[0,0].text(0.5, 0.5, 'No rating data', ha='center', va='center')
else:
    axes[0,0].text(0.5, 0.5, 'No rating column', ha='center', va='center')
axes[0,0].set_title('Movie Ratings Distribution', fontsize=14, fontweight='bold')
axes[0,0].set_xlabel('Rating')
axes[0,0].set_ylabel('Count')

# Genre frequency
if 'clean_genres' in movies_df.columns:
    genres = [g for sublist in movies_df['clean_genres'].dropna() for g in sublist]
    if genres:
        pd.Series(genres).value_counts().head(10).plot(kind='bar', ax=axes[0,1], color='lightgreen')
    else:
        axes[0,1].text(0.5, 0.5, 'No genre data', ha='center', va='center')
else:
    axes[0,1].text(0.5, 0.5, 'No genre column', ha='center', va='center')
axes[0,1].set_title('Top 10 Genres', fontsize=14, fontweight='bold')
axes[0,1].set_ylabel('Count')
axes[0,1].tick_params(axis='x', rotation=45)

# Movies per year
if 'release_year' in movies_df.columns:
    years = movies_df['release_year'].dropna()
    years = years[years > 1900]
    if len(years) > 0:
        yearly_counts = years.value_counts().sort_index()
        axes[1,0].plot(yearly_counts.index, yearly_counts.values, color='orange', linewidth=2)
        if len(yearly_counts) > 10:
            axes[1,0].set_xticks(yearly_counts.index[::len(yearly_counts)//10])
    else:
        axes[1,0].text(0.5, 0.5, 'No year data', ha='center', va='center')
else:
    axes[1,0].text(0.5, 0.5, 'No year column', ha='center', va='center')
axes[1,0].set_title('Movies Per Year', fontsize=14, fontweight='bold')
axes[1,0].set_xlabel('Year')
axes[1,0].set_ylabel('Count')
axes[1,0].tick_params(axis='x', rotation=45)

# Rating trends over time
if 'release_year' in movies_df.columns and 'numeric_rating' in movies_df.columns:
    data = movies_df[['release_year', 'numeric_rating']].dropna()
    data = data[data['release_year'] > 1900]
    if len(data) > 0:
        yearly_avg = data.groupby('release_year')['numeric_rating'].mean()
        axes[1,1].plot(yearly_avg.index, yearly_avg.values, color='purple', linewidth=2, marker='o', markersize=3)
        if len(yearly_avg) > 1:
            trend = np.polyfit(yearly_avg.index, yearly_avg.values, 1)
            axes[1,1].plot(yearly_avg.index, np.poly1d(trend)(yearly_avg.index), "r--", alpha=0.8, label='Trend')
            axes[1,1].legend()
    else:
        axes[1,1].text(0.5, 0.5, 'No data for trend', ha='center', va='center')
else:
    axes[1,1].text(0.5, 0.5, 'Need rating and year data', ha='center', va='center')
axes[1,1].set_title('Rating Trends Over Time', fontsize=14, fontweight='bold')
axes[1,1].set_xlabel('Year')
axes[1,1].set_ylabel('Average Rating')

plt.tight_layout()
plt.savefig('movie_analysis_plots.png', dpi=300, bbox_inches='tight')
plt.show()

# Answer key questions
print("\n" + "="*50)
print("ANALYSIS RESULTS")
print("="*50)

# Correlation between rating types
print("\nRating Correlations:")
if len(rating_cols) >= 2:
    for i in range(len(rating_cols)):
        for j in range(i+1, len(rating_cols)):
            col1, col2 = rating_cols[i], rating_cols[j]
            data1 = pd.to_numeric(movies_df[col1], errors='coerce')
            data2 = pd.to_numeric(movies_df[col2], errors='coerce')
            valid_data = pd.DataFrame({col1: data1, col2: data2}).dropna()
            if len(valid_data) > 10:
                corr, p_val = pearsonr(valid_data[col1], valid_data[col2])
                sig = 'Significant' if p_val < 0.05 else 'Not significant'
                print(f"  {col1} vs {col2}: {corr:.3f} (p={p_val:.4f}, {sig})")
else:
    print("  Need multiple rating columns for correlation")

# Genre ratings analysis
print("\nTop Genres by Rating:")
if 'clean_genres' in movies_df.columns and 'numeric_rating' in movies_df.columns:
    genre_ratings = []
    for _, row in movies_df.dropna(subset=['clean_genres', 'numeric_rating']).iterrows():
        for genre in row['clean_genres']:
            genre_ratings.append({'genre': genre, 'rating': row['numeric_rating']})
    
    if genre_ratings:
        genre_stats = pd.DataFrame(genre_ratings).groupby('genre')['rating'].agg(['mean', 'count']).round(3)
        genre_stats = genre_stats[genre_stats['count'] >= 5].sort_values('mean', ascending=False)
        print(genre_stats.head(10))
    else:
        print("  No genre-rating data available")
else:
    print("  Need both genre and rating data")

# Top movies
print("\nHighest Rated Movies:")
if 'numeric_rating' in movies_df.columns and main_title:
    top_movies = movies_df.nlargest(5, 'numeric_rating')[[main_title, 'numeric_rating']]
    for _, row in top_movies.iterrows():
        print(f"  {row[main_title]}: {row['numeric_rating']:.1f}")

print("\nAnalysis complete!")